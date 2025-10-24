"""
Full Performance Benchmark
==========================

Comprehensive benchmark testing up to 10M elements.
Generates plots and detailed performance analysis.

Usage: python benchmarks/full_benchmark.py
Runtime: 70-100 minutes
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

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("\\n  Warning: matplotlib not installed. Plots will not be generated.")
    print("Install with: pip install matplotlib\\n")


def run_comprehensive_benchmark():
    """Run comprehensive performance benchmark."""
    print("\\n" + "="*70)
    print("COMPREHENSIVE PERFORMANCE BENCHMARK")
    print("="*70)
    print("\\nTesting: Trie, Fenwick Tree, and Skip List")
    print("Dataset sizes: 1K to 10M elements")
    print("  This will take 80 minutes!")
    print("="*70)
    
    # Test sizes
    sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
    
    results = {
        'Trie': {'insert': [], 'search': []},
        'Fenwick': {'build': [], 'query': []},
        'SkipList': {'insert': [], 'search': []}
    }
    
    for idx, size in enumerate(sizes):
        print(f"\\n{'='*70}")
        print(f"[{idx+1}/{len(sizes)}] Testing with {size:,} elements...")
        print(f"{'='*70}")
        
        # Test Trie
        print(f"\\n[1/3] Trie (Prefix Tree)...")
        words = DataGenerator.generate_words(size)
        
        trie = Trie()
        start = time.time()
        for word in words:
            trie.insert(word)
        insert_time = time.time() - start
        results['Trie']['insert'].append(insert_time)
        
        search_words = random.sample(words, min(1000, len(words)))
        start = time.time()
        for word in search_words:
            trie.search(word)
        search_time = time.time() - start
        results['Trie']['search'].append(search_time)
        
        print(f"  Insert: {insert_time:.4f}s | Search: {search_time:.4f}s")
        
        # Test Fenwick Tree
        print(f"\\n[2/3] Fenwick Tree (Binary Indexed Tree)...")
        arr = DataGenerator.generate_array(size)
        
        ft = FenwickTree(size)
        start = time.time()
        ft.build_from_array(arr)
        build_time = time.time() - start
        results['Fenwick']['build'].append(build_time)
        
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
        
        sl = SkipList()
        start = time.time()
        for val in values:
            sl.insert(val)
        insert_time = time.time() - start
        results['SkipList']['insert'].append(insert_time)
        
        search_vals = random.sample(values, min(1000, len(values)))
        start = time.time()
        for val in search_vals:
            sl.search(val)
        search_time = time.time() - start
        results['SkipList']['search'].append(search_time)
        
        print(f"  Insert: {insert_time:.4f}s | Search: {search_time:.4f}s")
    
    # Generate visualizations
    if HAS_MATPLOTLIB:
        plot_results(sizes, results)
    
    print_summary_table(sizes, results)
    print_complexity_analysis()
    
    print("\\n" + "="*70)
    print(" FULL BENCHMARK COMPLETE!")
    print("="*70)


def plot_results(sizes, results):
    """Generate performance visualization plots."""
    print("\\n" + "="*70)
    print("GENERATING PLOTS")
    print("="*70)
    
    # Create results directory if it doesn't exist
    os.makedirs('results/plots', exist_ok=True)
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Advanced Data Structures Performance Comparison', 
                 fontsize=16, fontweight='bold')
    
    # Trie Insert
    axes[0, 0].plot(sizes, results['Trie']['insert'], marker='o', 
                   color='#2E86AB', linewidth=2)
    axes[0, 0].set_xlabel('Number of Words')
    axes[0, 0].set_ylabel('Time (seconds)')
    axes[0, 0].set_title('Trie - Insert Performance')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xscale('log')
    
    # Trie Search
    axes[1, 0].plot(sizes, results['Trie']['search'], marker='o', 
                   color='#A23B72', linewidth=2)
    axes[1, 0].set_xlabel('Number of Words')
    axes[1, 0].set_ylabel('Time (seconds)')
    axes[1, 0].set_title('Trie - Search Performance')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xscale('log')
    
    # Fenwick Build
    axes[0, 1].plot(sizes, results['Fenwick']['build'], marker='s', 
                   color='#F18F01', linewidth=2)
    axes[0, 1].set_xlabel('Array Size')
    axes[0, 1].set_ylabel('Time (seconds)')
    axes[0, 1].set_title('Fenwick Tree - Build Performance')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xscale('log')
    
    # Fenwick Query
    axes[1, 1].plot(sizes, results['Fenwick']['query'], marker='s', 
                   color='#C73E1D', linewidth=2)
    axes[1, 1].set_xlabel('Array Size')
    axes[1, 1].set_ylabel('Time (seconds)')
    axes[1, 1].set_title('Fenwick Tree - Query Performance')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xscale('log')
    
    # Skip List Insert
    axes[0, 2].plot(sizes, results['SkipList']['insert'], marker='^', 
                   color='#06A77D', linewidth=2)
    axes[0, 2].set_xlabel('Number of Elements')
    axes[0, 2].set_ylabel('Time (seconds)')
    axes[0, 2].set_title('Skip List - Insert Performance')
    axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].set_xscale('log')
    
    # Skip List Search
    axes[1, 2].plot(sizes, results['SkipList']['search'], marker='^', 
                   color='#005F73', linewidth=2)
    axes[1, 2].set_xlabel('Number of Elements')
    axes[1, 2].set_ylabel('Time (seconds)')
    axes[1, 2].set_title('Skip List - Search Performance')
    axes[1, 2].grid(True, alpha=0.3)
    axes[1, 2].set_xscale('log')
    
    plt.tight_layout()
    plt.savefig('results/plots/performance_comparison.png', dpi=300, bbox_inches='tight')
    print("\\n Performance plots saved to 'results/plots/performance_comparison.png'")
    
    # Comparison plot
    plt.figure(figsize=(15, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, results['Trie']['insert'], marker='o', label='Trie', linewidth=2)
    plt.plot(sizes, results['Fenwick']['build'], marker='s', label='Fenwick Tree', linewidth=2)
    plt.plot(sizes, results['SkipList']['insert'], marker='^', label='Skip List', linewidth=2)
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (seconds)')
    plt.title('Insert/Build Operation Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    plt.subplot(1, 2, 2)
    plt.plot(sizes, results['Trie']['search'], marker='o', label='Trie', linewidth=2)
    plt.plot(sizes, results['Fenwick']['query'], marker='s', label='Fenwick Tree', linewidth=2)
    plt.plot(sizes, results['SkipList']['search'], marker='^', label='Skip List', linewidth=2)
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (seconds)')
    plt.title('Search/Query Operation Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    plt.tight_layout()
    plt.savefig('results/plots/comparison_summary.png', dpi=300, bbox_inches='tight')
    print(" Comparison plots saved to 'results/plots/comparison_summary.png'")


def print_summary_table(sizes, results):
    """Print formatted performance summary table."""
    print("\\n" + "="*90)
    print("PERFORMANCE SUMMARY TABLE")
    print("="*90)
    print(f"\\n{'Size':<12} {'Data Structure':<15} {'Insert/Build':<15} {'Search/Query':<15}")
    print("-"*90)
    
    for i, size in enumerate(sizes):
        print(f"{size:<12,} {'Trie':<15} {results['Trie']['insert'][i]:<15.4f} {results['Trie']['search'][i]:<15.4f}")
        print(f"{'':12} {'Fenwick Tree':<15} {results['Fenwick']['build'][i]:<15.4f} {results['Fenwick']['query'][i]:<15.4f}")
        print(f"{'':12} {'Skip List':<15} {results['SkipList']['insert'][i]:<15.4f} {results['SkipList']['search'][i]:<15.4f}")
        print()


def print_complexity_analysis():
    """Print theoretical complexity analysis."""
    print("\n" + "="*90)
    print("THEORETICAL COMPLEXITY ANALYSIS")
    print("="*90)
    
    analysis = """
TRIE (PREFIX TREE):
------------------
Time Complexity:
  • Insert: O(m) where m = word length
  • Search: O(m) where m = word length
  • Prefix Search: O(p) where p = prefix length
  • Delete: O(m) where m = word length

Space Complexity: O(ALPHABET_SIZE x N x M) = O(total characters)

FENWICK TREE (BINARY INDEXED TREE):
-----------------------------------
Time Complexity:
  • Update: O(log n)
  • Prefix Sum Query: O(log n)
  • Range Sum Query: O(log n)
  • Build: O(n log n)

Space Complexity: O(n)

SKIP LIST:
----------
Time Complexity:
  • Insert: O(log n) average, O(n) worst case
  • Search: O(log n) average, O(n) worst case
  • Delete: O(log n) average, O(n) worst case

Space Complexity: O(n) expected, O(n log n) worst case
"""
    print(analysis)


if __name__ == "__main__":
    import functools
    print = functools.partial(print, flush=True)  # Auto-flush for nohup
    
    print("\n" + "="*70)
    print(" FULL PERFORMANCE BENCHMARK")
    print("="*70)
    print("\n  WARNING: This will take 10-20 minutes!")
    print("="*70)
    
    try:
        run_comprehensive_benchmark()
    except Exception as e:
        print(f"\n ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)