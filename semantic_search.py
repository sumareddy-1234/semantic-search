import argparse
import json
import sys
import time
from pathlib import Path
from typing import List, Dict, Tuple

import numpy as np
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
EMB_FILE = "embeddings.npy"
META_FILE = "metadata.json"
MODEL_FILE = "model_name.txt"

def load_txt_files(input_dir: Path, min_docs: int = 100) -> List[Path]:
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    files = sorted([p for p in input_dir.rglob("*.txt") if p.is_file()])
    if len(files) < min_docs:
        print(f"Warning: Found {len(files)} .txt files (minimum recommended: {min_docs}).", file=sys.stderr)
    return files

def read_file(path: Path, encoding: str = "utf-8") -> str:
    try:
        return path.read_text(encoding=encoding, errors="ignore")
    except Exception as e:
        raise IOError(f"Failed to read {path}: {e}")

def make_snippet(text: str, max_chars: int = 200) -> str:
    t = " ".join(text.split())
    return t[:max_chars] + ("..." if len(t) > max_chars else "")

def embed_corpus(model: SentenceTransformer, docs: List[str], batch_size: int = 64, show_progress: bool = True) -> np.ndarray:
    embeddings = []
    total = len(docs)
    for i in tqdm(range(0, total, batch_size), disable=not show_progress, desc="Embedding"):
        batch = docs[i:i + batch_size]
        emb = model.encode(batch, batch_size=batch_size, convert_to_numpy=True, normalize_embeddings=True)
        embeddings.append(emb)
    return np.vstack(embeddings)

def save_index(index_dir: Path, embeddings: np.ndarray, metadata: Dict, model_name: str):
    index_dir.mkdir(parents=True, exist_ok=True)
    np.save(index_dir / EMB_FILE, embeddings)
    (index_dir / META_FILE).write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    (index_dir / MODEL_FILE).write_text(model_name, encoding="utf-8")

def load_index(index_dir: Path) -> Tuple[np.ndarray, Dict, str]:
    emb_path = index_dir / EMB_FILE
    meta_path = index_dir / META_FILE
    model_path = index_dir / MODEL_FILE
    if not emb_path.exists() or not meta_path.exists():
        raise FileNotFoundError(f"Index not found in {index_dir}. Expected {EMB_FILE} and {META_FILE}.")
    embeddings = np.load(emb_path)
    metadata = json.loads(meta_path.read_text(encoding="utf-8"))
    model_name = model_path.read_text(encoding="utf-8") if model_path.exists() else DEFAULT_MODEL
    return embeddings, metadata, model_name

def index_directory(input_dir: Path, index_dir: Path, model_name: str = DEFAULT_MODEL, batch_size: int = 64):
    print(f"Loading model: {model_name}")
    model = SentenceTransformer(model_name)
    print(f"Ingesting documents from: {input_dir}")
    file_paths = load_txt_files(input_dir)
    if not file_paths:
        print("No .txt files found.", file=sys.stderr)
        return
    texts, ids, snippets = [], [], []
    for p in tqdm(file_paths, desc="Reading"):
        txt = read_file(p)
        texts.append(txt)
        ids.append(str(p.relative_to(input_dir)))
        snippets.append(make_snippet(txt))
    start = time.time()
    embeddings = embed_corpus(model, texts, batch_size=batch_size, show_progress=True)
    dur = time.time() - start
    print(f"Indexed {len(texts)} documents. Embedding time: {dur:.2f}s")
    metadata = {
        "doc_ids": ids,
        "base_dir": str(input_dir.resolve()),
        "snippets": {id_: snip for id_, snip in zip(ids, snippets)},
    }
    save_index(index_dir, embeddings, metadata, model_name)
    print(f"Index saved to {index_dir}")

def search(index_dir: Path, query: str, top_k: int = 5) -> List[Dict]:
    embeddings, metadata, model_name = load_index(index_dir)
    model = SentenceTransformer(model_name)
    q_emb = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    sims = cosine_similarity(q_emb, embeddings)[0]
    top_idx = np.argsort(-sims)[:top_k]
    results = []
    for i in top_idx:
        doc_id = metadata["doc_ids"][int(i)]
        results.append({
            "doc_id": doc_id,
            "score": float(sims[int(i)]),
            "snippet": metadata["snippets"].get(doc_id, "")
        })
    return results

def batch_search(index_dir: Path, queries_file: Path, top_k: int = 5) -> Dict[str, List[Dict]]:
    embeddings, metadata, model_name = load_index(index_dir)
    model = SentenceTransformer(model_name)
    if not queries_file.exists():
        raise FileNotFoundError(f"Queries file not found: {queries_file}")
    queries = [line.strip() for line in queries_file.read_text(encoding="utf-8").splitlines() if line.strip()]
    q_embs = model.encode(queries, convert_to_numpy=True, normalize_embeddings=True)
    sims = cosine_similarity(q_embs, embeddings)
    results_by_query = {}
    for qi, q in enumerate(queries):
        scores = sims[qi]
        top_idx = np.argsort(-scores)[:top_k]
        results = []
        for i in top_idx:
            doc_id = metadata["doc_ids"][int(i)]
            results.append({
                "doc_id": doc_id,
                "score": float(scores[int(i)]),
                "snippet": metadata["snippets"].get(doc_id, "")
            })
        results_by_query[q] = results
    return results_by_query

def print_results(results: List[Dict]):
    for rank, r in enumerate(results, start=1):
        print(f"{rank}. {r['doc_id']}  |  score={r['score']:.4f}")
        print(f"   {r['snippet']}")

def main():
    parser = argparse.ArgumentParser(description="Semantic search over a directory of .txt documents.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_index = subparsers.add_parser("index", help="Index a directory of .txt files.")
    p_index.add_argument("--input_dir", type=Path, required=True, help="Directory with .txt documents.")
    p_index.add_argument("--index_dir", type=Path, required=True, help="Directory to save the index.")
    p_index.add_argument("--model", type=str, default=DEFAULT_MODEL, help="SentenceTransformer model name.")
    p_index.add_argument("--batch_size", type=int, default=64, help="Batch size for embedding.")

    p_search = subparsers.add_parser("search", help="Search the index with a single query.")
    p_search.add_argument("--index_dir", type=Path, required=True, help="Directory containing the index.")
    p_search.add_argument("--query", type=str, required=True, help="Query string.")
    p_search.add_argument("--top_k", type=int, default=5, help="Number of top results.")

    p_batch = subparsers.add_parser("batch", help="Batch search with queries from a file (one per line).")
    p_batch.add_argument("--index_dir", type=Path, required=True, help="Directory containing the index.")
    p_batch.add_argument("--queries_file", type=Path, required=True, help="Text file of queries.")
    p_batch.add_argument("--top_k", type=int, default=5, help="Number of top results per query.")

    args = parser.parse_args()

    try:
        if args.command == "index":
            index_directory(args.input_dir, args.index_dir, args.model, args.batch_size)
        elif args.command == "search":
            results = search(args.index_dir, args.query, args.top_k)
            print_results(results)
        elif args.command == "batch":
            all_results = batch_search(args.index_dir, args.queries_file, args.top_k)
            for q, results in all_results.items():
                print(f"\nQuery: {q}")
                print_results(results)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
