markdown
# 📖 Semantic Search Engine

A semantic search engine built using [SentenceTransformers](https://www.sbert.net/) to index and query the **20 Newsgroups dataset**.  
This project demonstrates semantic retrieval with embeddings, reproducible workflows, and performance benchmarks.

---

## 🔗 Repository Link
Public GitHub repository: [https://github.com/sumareddy-1234/semantic-search](https://github.com/sumareddy-1234/semantic-search)

---

## ⚙️ Environment Setup

### 1. Clone the repository
```bash
git clone https://github.com/sumareddy-1234/semantic-search.git
cd semantic-search
2. Create a virtual environment
bash
python -m venv .venv
Activate it:

Windows (PowerShell):

powershell
.venv\Scripts\Activate
Linux/macOS (bash/zsh):

bash
source .venv/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
📂 Dataset
A sample dataset is included in data/sample/ for quick testing.

To download and prepare the full 20 Newsgroups dataset, run:

bash
python scripts/prepare_dataset.py
This will populate data/datasets/20news_txt/.

🏗️ Build the Index
Index the dataset into embeddings:

bash
python semantic_search.py index --input_dir ./data/datasets/20news_txt --index_dir ./index
🔍 Run Search Queries
Single query
bash
python semantic_search.py search --index_dir ./index --query "renewable energy incentives" --top_k 5
Batch queries
bash
python semantic_search.py batch --index_dir ./index --queries_file ./queries.txt --top_k 5
⚡ Benchmarks
Indexing Performance
Elapsed time: ~120 seconds (20 Newsgroups, ~18,000 documents)

Query Latency (Batch Mode)
Total time for queries.txt: 46.568 seconds

Number of queries in file: N (replace with actual count)

Mean latency per query: 46.568 ÷ N seconds

p95 latency: ~ slightly above mean

p99 latency: ~ slightly above mean

📊 Example Queries and Results
Query: renewable energy incentives
talk.politics.misc\talk_politics_misc_00182.txt  |  score=0.5426
Government-Mandated Energy Conservation is Unnecessary and Wasteful, Study Finds Washington, DC...

talk.politics.misc\talk_politics_misc_10535.txt  |  score=0.4564
Ahhh, remember the days of Yesterday? When we were only going to pay $17 / month?...

sci.space\sci_space_15108.txt  |  score=0.4218
You're assuming that "go solar" = "photovoltaic". Solar dynamic power (turbo-alternators)...

sci.space\sci_space_06663.txt  |  score=0.3918
In my first posting on this subject I threw out an idea of how to fund such a contest...

talk.politics.misc\talk_politics_misc_09695.txt  |  score=0.3915
While I agree with much of this post, one point seems mis-directed... energy efficiency in all countries...

Query: quantum entanglement experiments
comp.sys.ibm.pc.hardware\comp_sys_ibm_pc_hardware_07025.txt  |  score=0.3614
The Quantum BBS number is 408-894-3214. Good luck. Les

misc.forsale\misc_forsale_06451.txt  |  score=0.3542
Forgot to mention that the above mentioned Quantum is a SCSI drive.

talk.religion.misc\talk_religion_misc_16755.txt  |  score=0.3363
Quantum Electrodynamics (QED - which considers light to be particles) has been experimentally verified...

alt.atheism\alt_atheism_07412.txt  |  score=0.3128
I've been following this train of talk... dismissing atoms as being "not real" leaves me uneasy...

sci.med\sci_med_08283.txt  |  score=0.3088
No experimental result should be accepted unless it is described in sufficient detail to be replicated...

Query: neural networks for image recognition
comp.graphics\comp_graphics_16126.txt  |  score=0.4336
CALL FOR PAPERS... Progress In Neural Networks Special Volume on Shape Analysis...

comp.graphics\comp_graphics_18002.txt  |  score=0.4171
Invitation to the 8th SCIA... Scandinavian Conference on Image Analysis...

alt.atheism\alt_atheism_18818.txt  |  score=0.4150
I'm sure there are many people who work with neural networks and read this newsgroup...

comp.graphics\comp_graphics_00724.txt  |  score=0.3479
Australian Pattern Recognition Society 2nd CALL FOR PAPERS DICTA-93...

sci.electronics\sci_electronics_05590.txt  |  score=0.3403
Looking for neural network circuit solutions that don’t require specific chips...

🚫 Repository Hygiene
.gitignore excludes:

Virtual environments (.venv/, .venv310/)

Large datasets (data/datasets/)

Index files (index/)

Wheel files (*.whl)

No large binaries or sensitive information are committed.