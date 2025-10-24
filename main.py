"""
Main Entry Point
================

Central script to run tests, benchmarks, or demos.

Usage: python main.py
"""

import sys
import os


def main():
    """Main entry point with menu."""
    print("\n" + "="*70)
    print(" ADVANCED DATA STRUCTURES PROJECT")
    print("="*70)
    print("\nImplementations:")
    print("  • Trie (Prefix Tree)")
    print("  • Fenwick Tree (Binary Indexed Tree)")
    print("  • Skip List")
    print("="*70)
    
    while True:
        print("\n" + "="*70)
        print("MAIN MENU")
        print("="*70)
        print("1. Run Interactive Demo")
        print("2. Run Unit Tests")
        print("3. Run Quick Benchmark (~30 seconds)")
        print("4. Run Full Benchmark (~80 minutes)")
        print("5. Exit")
        print("="*70)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n" + "="*70)
            print("LOADING INTERACTIVE DEMO...")
            print("="*70)
            os.system('python demo.py')
            
        elif choice == '2':
            print("\n" + "="*70)
            print("RUNNING UNIT TESTS...")
            print("="*70)
            os.system('python -m pytest tests/ -v')
            
        elif choice == '3':
            print("\n" + "="*70)
            print("RUNNING QUICK BENCHMARK...")
            print("="*70)
            os.system('python benchmarks/quick_benchmark.py')
            
        elif choice == '4':
            print("\n" + "="*70)
            print("  WARNING: Full benchmark takes 80 minutes!")
            print("="*70)
            confirm = input("Continue? (yes/no): ").strip().lower()
            if confirm in ['yes', 'y']:
                os.system('python benchmarks/full_benchmark.py')
            else:
                print("Cancelled.")
                
        elif choice == '5':
            print("\n" + "="*70)
            print("Thank you!")
            print("="*70)
            break
            
        else:
            print("\n Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()