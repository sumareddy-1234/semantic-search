import argparse
from pathlib import Path
from sklearn.datasets import fetch_20newsgroups

def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text or "", encoding="utf-8", errors="ignore")

def sanitize(s: str) -> str:
    return "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in s)

def prepare_20newsgroups(output_dir: Path, min_docs: int):
    ds = fetch_20newsgroups(subset="all", remove=("headers", "footers", "quotes"))
    count = 0
    for i, text in enumerate(ds.data):
        target = ds.target_names[ds.target[i]]
        fname = f"{sanitize(target)}_{i:05d}.txt"
        write_text(output_dir / target / fname, text)
        count += 1
    print(f"Wrote {count} docs to {output_dir}")
    if count < min_docs:
        print(f"Warning: only {count} docs (min recommended: {min_docs})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output_dir", type=Path, required=True)
    ap.add_argument("--min_docs", type=int, default=100)
    args = ap.parse_args()
    prepare_20newsgroups(args.output_dir, args.min_docs)

if __name__ == "__main__":
    main()
