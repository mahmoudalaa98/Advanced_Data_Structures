import json
import os
import sys
from datetime import datetime
from src.utils import DataGenerator


def generate_datasets():
    """Generate all benchmark datasets."""
    
    print("\n" + "="*70)
    print("GENERATING BENCHMARK DATASETS")
    print("="*70)
    
    # Create output directory
    os.makedirs('datasets', exist_ok=True)
    
    # Dataset sizes to generate (1K to 10M elements)
    sizes = [1000, 10000, 100000, 1000000, 5000000, 10000000]
    
    total_size_mb = 0
    files_created = []
    
    # Generate datasets for each size
    for idx, size in enumerate(sizes):
        print(f"\n[{idx+1}/{len(sizes)}] Generating {size:,} elements...")
        
        # Trie dataset: random words
        words = DataGenerator.generate_words(size)
        filename = f'datasets/trie_words_{size}.json'
        with open(filename, 'w') as f:
            json.dump(words, f)
        file_size = os.path.getsize(filename) / (1024 * 1024)
        total_size_mb += file_size
        files_created.append(filename)
        print(f"  Trie: {filename} ({file_size:.2f} MB)")
        
        # Fenwick Tree dataset: random integers
        array = DataGenerator.generate_array(size)
        filename = f'datasets/fenwick_array_{size}.json'
        with open(filename, 'w') as f:
            json.dump(array, f)
        file_size = os.path.getsize(filename) / (1024 * 1024)
        total_size_mb += file_size
        files_created.append(filename)
        print(f"   Fenwick: {filename} ({file_size:.2f} MB)")
        
        # Skip List dataset: random integers
        integers = DataGenerator.generate_integers(size)
        filename = f'datasets/skiplist_integers_{size}.json'
        with open(filename, 'w') as f:
            json.dump(integers, f)
        file_size = os.path.getsize(filename) / (1024 * 1024)
        total_size_mb += file_size
        files_created.append(filename)
        print(f"   Skip List: {filename} ({file_size:.2f} MB)")
    
    # Save metadata
    metadata = {
        "generation_date": datetime.now().isoformat(),
        "sizes": sizes,
        "total_files": len(files_created),
        "total_size_mb": round(total_size_mb, 2)
    }
    with open('datasets/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"COMPLETE: {len(files_created)} files created ({total_size_mb:.2f} MB)")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    try:
        generate_datasets()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)