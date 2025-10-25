# COSC 520 – Advanced Data Structures Assignment 2

This repository contains the implementation and performance comparison of three advanced data structures: Trie (Prefix Tree), Fenwick Tree (Binary Indexed Tree), and Skip List. Developed for COSC 520 – Advanced Data Structures at the University of British Columbia.

## 📘 Overview

The goal of this assignment is to explore advanced data structures and benchmark their performance. Each structure is implemented from scratch and tested on synthetic datasets of different sizes to analyze time complexity and scalability.

## 🧩 Implemented Data Structures

*   **Trie (Prefix Tree)** – efficient prefix-based word search
*   **Fenwick Tree (Binary Indexed Tree)** – fast prefix-sum and update operations
*   **Skip List** – probabilistic balanced structure for ordered data

## ⚙️ Running the Code

### Setup

Dataset: https://drive.google.com/drive/folders/1TJMR997f9C9nVq57FmbMqFKyZDVFJYm5?usp=drive_link

```bash
# Clone the repository
git clone https://github.com/mahmoudalaa98/Advanced_Data_Structures.git

# Navigate to the project directory
cd Advanced_Data_Structures

# Install dependencies
pip install -r requirements.txt
```

### Run Benchmarks

To run the comprehensive benchmark script:

```bash
python benchmarks/full_benchmark.py
```

This script benchmarks all three data structures and saves the resulting plots in the results/plots/ folder.

### Run Unit Tests

To run all unit tests for the data structures:

```bash
python -m unittest discover tests
```

## 📁 Project Structure

```
Advanced_Data_Structures/
│
├── benchmarks/
│   ├── __init__.py
│   ├── full_benchmark.py
│   └── quick_benchmark.py
│
├── results/
│   └── plots/
│       ├── comparison_summary.png
│       └── performance_comparison.png
│
├── src/
│   ├── __init__.py
│   ├── fenwick_tree.py
│   ├── skip_list.py
│   ├── trie.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_fenwick_tree.py
│   ├── test_skip_list.py
│   └── test_trie.py
│
└── requirements.txt
```

## 📊 Summary of Findings

| Data Structure | Strength | Typical Use Case |
|----------------|----------|------------------|
| Trie | Fast string search, prefix queries | Dictionaries, autocomplete |
| Fenwick Tree | Efficient numeric range queries | Frequency counts, range sums |
| Skip List | Balanced performance and simplicity | Ordered maps, database indexes |

## 📚 References

* Cormen et al., Introduction to Algorithms (3rd Ed.)
* GeeksforGeeks – Advanced Data Structures
* Opengenus – Data Structure Implementations

Note: This repository is part of the COSC 520 course assignment and is intended for academic evaluation only.

