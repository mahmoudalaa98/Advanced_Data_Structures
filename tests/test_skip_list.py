"""
Unit Tests for Skip List
=========================

Run with: python -m pytest tests/test_skip_list.py -v
Or directly: python tests/test_skip_list.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src.skip_list import SkipList


class TestSkipList:
    """Comprehensive Skip List tests."""
    
    def test_basic_operations(self):
        """Test basic insert operations."""
        sl = SkipList()
        values = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
        
        for val in values:
            sl.insert(val)
        
        assert sl.size == len(values), f"Size mismatch: {sl.size} vs {len(values)}"
    
    def test_search_operations(self):
        """Test search operations."""
        sl = SkipList()
        values = [5, 10, 15, 20, 25]
        
        for val in values:
            sl.insert(val)
        
        # Search existing values
        for val in values:
            assert sl.search(val), f"Failed to find {val}"
        
        # Search non-existing values
        assert not sl.search(7), "Found non-existent value 7"
        assert not sl.search(100), "Found non-existent value 100"
    
    def test_delete_operations(self):
        """Test delete operations."""
        sl = SkipList()
        values = [1, 2, 3, 4, 5]
        
        for val in values:
            sl.insert(val)
        
        # Delete middle value
        assert sl.delete(3), "Delete failed"
        assert not sl.search(3), "Deleted value still found"
        assert sl.size == 4, "Size not updated"
        
        # Delete first value
        assert sl.delete(1), "Delete first failed"
        assert not sl.search(1), "Deleted first value still found"
        
        # Delete last value
        assert sl.delete(5), "Delete last failed"
        assert not sl.search(5), "Deleted last value still found"
        
        # Try to delete non-existent
        assert not sl.delete(10), "Delete of non-existent should return False"
    
    def test_duplicate_handling(self):
        """Test handling of duplicate values."""
        sl = SkipList()
        
        sl.insert(5)
        sl.insert(5)  # Duplicate
        
        # Should allow duplicates or handle gracefully
        assert sl.search(5), "Value not found after duplicate insert"
    
    def test_large_dataset(self):
        """Test with large dataset."""
        sl = SkipList()
        values = list(range(0, 1000, 2))  # Even numbers from 0 to 998
        
        for val in values:
            sl.insert(val)
        
        # Search some values
        assert sl.search(500), "Failed to find 500"
        assert sl.search(0), "Failed to find 0"
        assert sl.search(998), "Failed to find 998"
        assert not sl.search(501), "Found non-existent odd number"
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Empty list
        sl_empty = SkipList()
        assert not sl_empty.search(1), "Empty list search should return False"
        assert not sl_empty.delete(1), "Empty list delete should return False"
        
        # Single element
        sl_single = SkipList()
        sl_single.insert(42)
        assert sl_single.search(42), "Single element not found"
        assert sl_single.delete(42), "Single element delete failed"
        assert not sl_single.search(42), "Deleted single element still found"
        
        # Negative numbers
        sl_neg = SkipList()
        sl_neg.insert(-5)
        sl_neg.insert(-10)
        assert sl_neg.search(-5), "Negative number not found"
        assert sl_neg.search(-10), "Negative number not found"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


print("\n" + "="*70)
print("CREATING BENCHMARK FILES")
print("="*70 + "\n")