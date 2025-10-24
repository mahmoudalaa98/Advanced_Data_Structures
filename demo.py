"""
Interactive Demo
================

Demonstrates all three data structures with examples.

Usage: python demo.py
"""

from src.trie import Trie
from src.fenwick_tree import FenwickTree
from src.skip_list import SkipList


def demo_trie():
    """Demonstrate Trie operations."""
    print("\n" + "="*70)
    print("TRIE (PREFIX TREE) DEMO")
    print("="*70)
    
    trie = Trie()
    
    print("\n1. Inserting words: ['hello', 'world', 'help', 'heap', 'wonder']")
    words = ["hello", "world", "help", "heap", "wonder"]
    for word in words:
        trie.insert(word)
    print(f"   Words inserted: {trie.word_count}")
    
    print("\n2. Searching for words:")
    print(f"   Search 'hello': {trie.search('hello')}")
    print(f"   Search 'hell': {trie.search('hell')} (not a complete word)")
    print(f"   Search 'world': {trie.search('world')}")
    
    print("\n3. Prefix search:")
    print(f"   Starts with 'hel': {trie.starts_with('hel')}")
    print(f"   Starts with 'wo': {trie.starts_with('wo')}")
    print(f"   Starts with 'xyz': {trie.starts_with('xyz')}")
    
    print("\n4. Get all words with prefix 'he':")
    words_with_he = trie.get_all_words_with_prefix('he')
    print(f"   Words: {words_with_he}")
    
    print("\n5. Delete 'hello':")
    trie.delete('hello')
    print(f"   Search 'hello': {trie.search('hello')}")
    print(f"   Search 'help': {trie.search('help')} (still exists)")
    print(f"   Total words: {trie.word_count}")


def demo_fenwick_tree():
    """Demonstrate Fenwick Tree operations."""
    print("\n" + "="*70)
    print("FENWICK TREE (BINARY INDEXED TREE) DEMO")
    print("="*70)
    
    print("\n1. Creating array: [1, 3, 5, 7, 9, 11]")
    arr = [1, 3, 5, 7, 9, 11]
    ft = FenwickTree(len(arr))
    ft.build_from_array(arr)
    
    print("\n2. Prefix sum queries:")
    print(f"   Sum of first 1 element (index 0): {ft.query(0)}")
    print(f"   Sum of first 3 elements (index 0-2): {ft.query(2)} = 1+3+5")
    print(f"   Sum of all elements (index 0-5): {ft.query(5)} = 1+3+5+7+9+11")
    
    print("\n3. Range sum queries:")
    print(f"   Sum of range [1, 3]: {ft.range_query(1, 3)} = 3+5+7")
    print(f"   Sum of range [2, 4]: {ft.range_query(2, 4)} = 5+7+9")
    
    print("\n4. Update operations:")
    print(f"   Adding 10 to index 2 (5 becomes 15)")
    ft.update(2, 10)
    print(f"   New sum of first 3 elements: {ft.query(2)} = 1+3+15")
    print(f"   New sum of all elements: {ft.query(5)}")
    
    print("\n5. Multiple updates:")
    ft.update(0, 5)  # Add 5 to first element
    ft.update(4, -4)  # Subtract 4 from element at index 4
    print(f"   After updates: sum of all = {ft.query(5)}")


def demo_skip_list():
    """Demonstrate Skip List operations."""
    print("\n" + "="*70)
    print("SKIP LIST DEMO")
    print("="*70)
    
    sl = SkipList()
    
    print("\n1. Inserting values: [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]")
    values = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
    for val in values:
        sl.insert(val)
    print(f"   Values inserted: {sl.size}")
    
    print("\n2. Searching for values:")
    print(f"   Search 7: {sl.search(7)}")
    print(f"   Search 12: {sl.search(12)}")
    print(f"   Search 10: {sl.search(10)} (not in list)")
    print(f"   Search 100: {sl.search(100)} (not in list)")
    
    print("\n3. Delete operations:")
    print(f"   Deleting 7: {sl.delete(7)}")
    print(f"   Search 7 after deletion: {sl.search(7)}")
    print(f"   Size after deletion: {sl.size}")
    
    print("\n4. More deletions:")
    print(f"   Deleting 3: {sl.delete(3)}")
    print(f"   Deleting 26: {sl.delete(26)}")
    print(f"   Size now: {sl.size}")
    
    print("\n5. Try to delete non-existent value:")
    print(f"   Deleting 100: {sl.delete(100)} (should be False)")
    
    print("\n6. Insert duplicate:")
    sl.insert(9)  # 9 already exists
    print(f"   Inserted 9 again (duplicates allowed)")
    print(f"   Search 9: {sl.search(9)}")


def main():
    """Main demo function."""
    print("\n" + "="*70)
    print(" ADVANCED DATA STRUCTURES - INTERACTIVE DEMO")
    print("="*70)
    print("\nThis demo shows the capabilities of three data structures:")
    print("  1. Trie (Prefix Tree) - for string operations")
    print("  2. Fenwick Tree (BIT) - for range sum queries")
    print("  3. Skip List - for probabilistic balanced structure")
    print("="*70)
    
    while True:
        print("\n" + "="*70)
        print("MENU")
        print("="*70)
        print("1. Demo Trie (Prefix Tree)")
        print("2. Demo Fenwick Tree (Binary Indexed Tree)")
        print("3. Demo Skip List")
        print("4. Demo All Structures")
        print("5. Exit")
        print("="*70)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            demo_trie()
        elif choice == '2':
            demo_fenwick_tree()
        elif choice == '3':
            demo_skip_list()
        elif choice == '4':
            demo_trie()
            demo_fenwick_tree()
            demo_skip_list()
            print("\n" + "="*70)
            print("✓ ALL DEMOS COMPLETE!")
            print("="*70)
        elif choice == '5':
            print("\n" + "="*70)
            print("Thank you for using the demo!")
            print("="*70)
            break
        else:
            print("\n❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()