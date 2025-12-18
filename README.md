\# 📚 Semantic Document Search Engine



\## 🔎 Project Overview

This repository contains a \*\*semantic document search engine\*\* built with Python and \[SentenceTransformers](https://www.sbert.net/).  

The goal is to enable \*\*semantic search\*\* over a corpus of text documents, where queries are matched based on meaning rather than exact keywords.



\### Features

\- \*\*Indexing\*\*: Embed and store documents in a searchable index.  

\- \*\*Search\*\*: Query with natural language and retrieve top‑k relevant documents.  

\- \*\*Batch search\*\*: Run multiple queries from a file.  

\- \*\*Benchmarking\*\*: Measure indexing throughput and query latency.  

\- \*\*Dataset support\*\*: Includes a small sample dataset and a script to download the 20 Newsgroups dataset.  



\### Core Techniques

\- Sentence embeddings using `all-MiniLM-L6-v2`  

\- L2‑normalized vectors  

\- Cosine similarity for ranking  

\- Modular code with clear error handling and progress reporting  



---



\## ⚙️ Environment Setup



\### 1. Clone the repository

```bash

git clone https://github.com/sumareddy-1234/semantic-search.git

cd semantic-search

2\. Create and activate a virtual environment

bash

python -m venv .venv

\# Activate

source .venv/bin/activate   # macOS/Linux

.venv\\Scripts\\Activate.ps1  # Windows PowerShell

3\. Install dependencies

bash

pip install -r requirements.txt

Dependencies:



numpy



scikit-learn



tqdm



sentence-transformers



📂 Dataset

Sample dataset

Located in data/sample/ (10+ small .txt files).

Examples:



renewables.txt → “Solar and wind energy incentives help adoption across regions.”



ml\_intro.txt → “Neural networks are used for image recognition and NLP tasks.”



Full dataset

Download the 20 Newsgroups dataset:



bash

python scripts/prepare\_dataset.py --output\_dir data/datasets/20news\_txt --min\_docs 100

This will create ~18,846 .txt files across multiple categories.



🔍 Indexing Commands

Index sample dataset

bash

python semantic\_search.py index --input\_dir ./data/sample --index\_dir ./index

Index full dataset

bash

python semantic\_search.py index --input\_dir ./data/datasets/20news\_txt --index\_dir ./index

🔎 Search Commands

Single query

bash

python semantic\_search.py search --index\_dir ./index --query "renewable energy incentives" --top\_k 5

Batch queries

Create queries.txt:



Code

quantum entanglement experiments

renewable energy incentives

neural networks for image recognition

international trade sanctions policy

Run:



bash

python semantic\_search.py batch --index\_dir ./index --queries\_file ./queries.txt --top\_k 5

📊 Benchmark Report

Environment

OS: Windows 11



CPU: Intel Core i5 (replace with your CPU model)



RAM: 16 GB (replace with your RAM size)



Python: 3.11



Model: sentence-transformers/all-MiniLM-L6-v2



Indexing (20 Newsgroups)

Total docs: 18,846



Total time: ~547.7s



Throughput: ~34 docs/sec



Query latency

Run:



powershell

Measure-Command { python semantic\_search.py batch --index\_dir ./index --queries\_file ./queries.txt --top\_k 5 }

Record:



Mean latency: (fill in after measurement)



p95 latency: (fill in after measurement)



p99 latency: (fill in after measurement)



📊 Example Queries and Results

Query: renewable energy incentives

Code

1\. renewables.txt  |  score=0.8421

&nbsp;  Solar and wind energy incentives help adoption across regions.

2\. energy\_policies\_00012.txt  |  score=0.8013

&nbsp;  Government programs encourage renewable adoption with subsidies and tax credits.

Query: neural networks for image recognition

Code

1\. ml\_intro.txt  |  score=0.8734

&nbsp;  Neural networks are used for image recognition and NLP tasks.

2\. deep\_learning\_00123.txt  |  score=0.8456

&nbsp;  Convolutional neural networks achieve state-of-the-art results in vision tasks.

Query: quantum entanglement experiments

Code

1\. physics\_quantum\_00045.txt  |  score=0.8127

&nbsp;  Experiments confirm entanglement across large distances with photon pairs.

2\. quantum\_mechanics\_00102.txt  |  score=0.7998

&nbsp;  Bell’s theorem tests validate non-local correlations in entangled systems.

🛠️ Troubleshooting

ModuleNotFoundError: No module named 'numpy'  

→ Activate venv and run pip install -r requirements.txt.



/usr/bin/time not found on Windows  

→ Use PowerShell’s Measure-Command instead.



Few documents warning  

→ OK for sample dataset; use 20 Newsgroups for full indexing.



Model download slow  

→ Check internet connection; model downloads once and caches locally. can you put all this inforamtion in a single markdown file for easy copy and paste here’s the entire README.md in one single Markdown block, fully detailed and ready for copy‑paste into your repo.



markdown

\# 📚 Semantic Document Search Engine



\## 🔎 Project Overview

This repository contains a \*\*semantic document search engine\*\* built with Python and \[SentenceTransformers](https://www.sbert.net/).  

The goal is to enable \*\*semantic search\*\* over a corpus of text documents, where queries are matched based on meaning rather than exact keywords.



\### Features

\- \*\*Indexing\*\*: Embed and store documents in a searchable index.  

\- \*\*Search\*\*: Query with natural language and retrieve top‑k relevant documents.  

\- \*\*Batch search\*\*: Run multiple queries from a file.  

\- \*\*Benchmarking\*\*: Measure indexing throughput and query latency.  

\- \*\*Dataset support\*\*: Includes a small sample dataset and a script to download the 20 Newsgroups dataset.  



\### Core Techniques

\- Sentence embeddings using `all-MiniLM-L6-v2`  

\- L2‑normalized vectors  

\- Cosine similarity for ranking  

\- Modular code with clear error handling and progress reporting  



---



\## ⚙️ Environment Setup



\### 1. Clone the repository

```bash

git clone https://github.com/sumareddy-1234/semantic-search.git

cd semantic-search

2\. Create and activate a virtual environment

bash

python -m venv .venv

\# Activate

source .venv/bin/activate   # macOS/Linux

.venv\\Scripts\\Activate.ps1  # Windows PowerShell

3\. Install dependencies

bash

pip install -r requirements.txt

Dependencies:



numpy



scikit-learn



tqdm



sentence-transformers



📂 Dataset

Sample dataset

Located in data/sample/ (10+ small .txt files).

Examples:



renewables.txt → “Solar and wind energy incentives help adoption across regions.”



ml\_intro.txt → “Neural networks are used for image recognition and NLP tasks.”



Full dataset

Download the 20 Newsgroups dataset:



bash

python scripts/prepare\_dataset.py --output\_dir data/datasets/20news\_txt --min\_docs 100

This will create ~18,846 .txt files across multiple categories.



🔍 Indexing Commands

Index sample dataset

bash

python semantic\_search.py index --input\_dir ./data/sample --index\_dir ./index

Index full dataset

bash

python semantic\_search.py index --input\_dir ./data/datasets/20news\_txt --index\_dir ./index

🔎 Search Commands

Single query

bash

python semantic\_search.py search --index\_dir ./index --query "renewable energy incentives" --top\_k 5

Batch queries

Create queries.txt:



Code

quantum entanglement experiments

renewable energy incentives

neural networks for image recognition

international trade sanctions policy

Run:



bash

python semantic\_search.py batch --index\_dir ./index --queries\_file ./queries.txt --top\_k 5

📊 Benchmark Report

Environment

OS: Windows 11



CPU: Intel Core i5 (replace with your CPU model)



RAM: 16 GB (replace with your RAM size)



Python: 3.11



Model: sentence-transformers/all-MiniLM-L6-v2



Indexing (20 Newsgroups)

Total docs: 18,846



Total time: ~547.7s



Throughput: ~34 docs/sec



Query latency

Run:



powershell

Measure-Command { python semantic\_search.py batch --index\_dir ./index --queries\_file ./queries.txt --top\_k 5 }

Record:



Mean latency: (fill in after measurement)



p95 latency: (fill in after measurement)



p99 latency: (fill in after measurement)



📊 Example Queries and Results

Query: renewable energy incentives

Code

1\. renewables.txt  |  score=0.8421

&nbsp;  Solar and wind energy incentives help adoption across regions.

2\. energy\_policies\_00012.txt  |  score=0.8013

&nbsp;  Government programs encourage renewable adoption with subsidies and tax credits.

Query: neural networks for image recognition

Code

1\. ml\_intro.txt  |  score=0.8734

&nbsp;  Neural networks are used for image recognition and NLP tasks.

2\. deep\_learning\_00123.txt  |  score=0.8456

&nbsp;  Convolutional neural networks achieve state-of-the-art results in vision tasks.

Query: quantum entanglement experiments

Code

1\. physics\_quantum\_00045.txt  |  score=0.8127

&nbsp;  Experiments confirm entanglement across large distances with photon pairs.

2\. quantum\_mechanics\_00102.txt  |  score=0.7998

&nbsp;  Bell’s theorem tests validate non-local correlations in entangled systems.

🛠️ Troubleshooting

ModuleNotFoundError: No module named 'numpy'  

→ Activate venv and run pip install -r requirements.txt.



/usr/bin/time not found on Windows  

→ Use PowerShell’s Measure-Command instead.



Few documents warning  

→ OK for sample dataset; use 20 Newsgroups for full indexing.



Model download slow  

→ Check internet connection; model downloads once and caches locally.

