"""
Quick Benchmark Script
======================

This script runs a fast benchmark with smaller datasets for quick testing.
Use this to verify everything works before running the full 10M element benchmark.

Usage: python benchmarks/quick_benchmark.py

Runtime: ~30 seconds
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import time
import random
from src.trie import Trie
from src.fenwick_tree import FenwickTree
from src.skip_list import SkipList
from src.utils import DataGenerator


def quick_benchmark():
    """Run quick benchmark with smaller datasets."""
    print("\\n" + "="*70)
    print(" QUICK BENCHMARK - TESTING MODE")
    print("="*70)
    print("\\nThis will test with smaller datasets (1K, 10K, 100K)")
    print("Estimated time: ~30 seconds")
    print("="*70 + "\\n")
    
    sizes = [1000, 10000, 100000]
    
    results = {
        'Trie': {'insert': [], 'search': []},
        'Fenwick': {'build': [], 'query': []},
        'SkipList': {'insert': [], 'search': []}
    }
    
    for size in sizes:
        print(f"\\n{'='*70}")
        print(f"Testing with {size:,} elements...")
        print(f"{'='*70}")
        
        # Test Trie
        print(f"\\n[1/3] Trie...")
        words = DataGenerator.generate_words(size)
        
        # Insert
        trie = Trie()
        start = time.time()
        for word in words:
            trie.insert(word)
        insert_time = time.time() - start
        results['Trie']['insert'].append(insert_time)
        
        # Search
        search_words = random.sample(words, min(1000, len(words)))
        start = time.time()
        for word in search_words:
            trie.search(word)
        search_time = time.time() - start
        results['Trie']['search'].append(search_time)
        
        print(f"  Insert: {insert_time:.4f}s | Search: {search_time:.4f}s")
        
        # Test Fenwick Tree
        print(f"\\n[2/3] Fenwick Tree...")
        arr = DataGenerator.generate_array(size)
        
        # Build
        ft = FenwickTree(len(arr))
        start = time.time()
        ft.build_from_array(arr)
        build_time = time.time() - start
        results['Fenwick']['build'].append(build_time)
        
        # Query
        queries = min(10000, size)
        start = time.time()
        for _ in range(queries):
            idx = random.randint(0, size - 1)
            ft.query(idx)
        query_time = time.time() - start
        results['Fenwick']['query'].append(query_time)
        
        print(f"  Build: {build_time:.4f}s | Query: {query_time:.4f}s")
        
        # Test Skip List
        print(f"\\n[3/3] Skip List...")
        values = DataGenerator.generate_integers(size)
        
        # Insert
        sl = SkipList()
        start = time.time()
        for val in values:
            sl.insert(val)
        insert_time = time.time() - start
        results['SkipList']['insert'].append(insert_time)
        
        # Search
        search_vals = random.sample(values, min(1000, len(values)))
        start = time.time()
        for val in search_vals:
            sl.search(val)
        search_time = time.time() - start
        results['SkipList']['search'].append(search_time)
        
        print(f"  Insert: {insert_time:.4f}s | Search: {search_time:.4f}s")
    
    # Print summary
    print("\\n" + "="*70)
    print("QUICK BENCHMARK SUMMARY")
    print("="*70)
    print(f"\\n{'Size':<12} {'Data Structure':<15} {'Insert/Build':<15} {'Search/Query':<15}")
    print("-"*70)
    
    for i, size in enumerate(sizes):
        print(f"{size:<12,} {'Trie':<15} {results['Trie']['insert'][i]:<15.4f} {results['Trie']['search'][i]:<15.4f}")
        print(f"{'':12} {'Fenwick Tree':<15} {results['Fenwick']['build'][i]:<15.4f} {results['Fenwick']['query'][i]:<15.4f}")
        print(f"{'':12} {'Skip List':<15} {results['SkipList']['insert'][i]:<15.4f} {results['SkipList']['search'][i]:<15.4f}")
        print()
    
    print("="*70)
    print("✓ QUICK BENCHMARK COMPLETE!")
    print("="*70)
    print("\\nTo run the full benchmark (up to 10M elements):")
    print("  python benchmarks/full_benchmark.py")
    print("="*70)


if __name__ == "__main__":
    print("\\n" + "="*70)
    print(" QUICK BENCHMARK SCRIPT")
    print("="*70)
    print("\\nThis will run a fast benchmark to verify everything works.")
    print("Use this before running the full benchmark with 10M elements.")
    print("="*70)
    
    input("\\nPress Enter to start quick benchmark...")
    
    try:
        quick_benchmark()
    except Exception as e:
        print(f"\\n❌ Error occurred: {e}")
        print("\\nPlease check that all files are in the correct directories.")
        import traceback
        traceback.print_exc()
def print_complexity_analysis():
    """Print theoretical complexity analysis."""
    print("\n" + "="*90)
    print("THEORETICAL COMPLEXITY ANALYSIS")
    print("="*90)
    
#     analysis = """
# TRIE (PREFIX TREE):
# ------------------
# Time Complexity:
#   • Insert: O(m) where m = word length
#   • Search: O(m) where m = word length
#   • Prefix Search: O(p) where p = prefix length
#   • Delete: O(m) where m = word length

# Space Complexity: O(ALPHABET_SIZE × N × M) = O(total characters)

# FENWICK TREE (BINARY INDEXED TREE):
# -----------------------------------
# Time Complexity:
#   • Update: O(log n)
#   • Prefix Sum Query: O(log n)
#   • Range Sum Query: O(log n)
#   • Build: O(n log n)

# Space Complexity: O(n)

# SKIP LIST:
# ----------
# Time Complexity:
#   • Insert: O(log n) average, O(n) worst case
#   • Search: O(log n) average, O(n) worst case
#   • Delete: O(log n) average, O(n) worst case

# Space Complexity: O(n) expected, O(n log n) worst case
# """
#     print(analysis)


if __name__ == "__main__":
    print("\n" + "="*70)
    print(" FULL PERFORMANCE BENCHMARK")
    print("="*70)
    print("\n⚠️  WARNING: This will take 10-20 minutes!")
    print("="*70)
    
    confirm = input("\nDo you want to continue? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        try:
            run_comprehensive_benchmark()
        except Exception as e:
            print(f"\n❌ Error occurred: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("\nBenchmark cancelled.")