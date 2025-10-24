"""
Unit Tests for Fenwick Tree
============================

Run with: python -m pytest tests/test_fenwick_tree.py -v
Or directly: python tests/test_fenwick_tree.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src.fenwick_tree import FenwickTree


class TestFenwickTree:
    """Comprehensive Fenwick Tree tests."""
    
    def test_basic_operations(self):
        """Test basic build and query."""
        arr = [1, 3, 5, 7, 9, 11]
        ft = FenwickTree(len(arr))
        ft.build_from_array(arr)
        
        assert ft.query(0) == 1, "Query(0) should be 1"
        assert ft.query(2) == 9, "Query(2) should be 1+3+5=9"
        assert ft.query(5) == 36, "Query(5) should be sum of all = 36"
    
    def test_update_operations(self):
        """Test update operations."""
        arr = [1, 2, 3, 4, 5]
        ft = FenwickTree(len(arr))
        ft.build_from_array(arr)
        
        # Update index 2
        ft.update(2, 10)  # Add 10 to index 2
        assert ft.query(2) == 1 + 2 + 3 + 10, "Update failed"
        
        # Multiple updates
        ft.update(0, 5)
        assert ft.query(0) == 1 + 5, "Multiple updates failed"
    
    def test_range_queries(self):
        """Test range query operations."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ft = FenwickTree(len(arr))
        ft.build_from_array(arr)
        
        # Range [0, 4] = 1+2+3+4+5 = 15
        assert ft.range_query(0, 4) == 15, "Range query [0,4] failed"
        
        # Range [2, 5] = 3+4+5+6 = 18
        assert ft.range_query(2, 5) == 18, "Range query [2,5] failed"
        
        # Range [0, 0] = 1
        assert ft.range_query(0, 0) == 1, "Range query [0,0] failed"
    
    def test_negative_values(self):
        """Test with negative values."""
        arr = [1, -2, 3, -4, 5]
        ft = FenwickTree(len(arr))
        ft.build_from_array(arr)
        
        # Sum = 1 + (-2) + 3 + (-4) + 5 = 3
        assert ft.query(4) == 3, "Negative values failed"
        
        # Update with negative value
        ft.update(0, -10)
        assert ft.query(0) == 1 + (-10), "Negative update failed"
    
    def test_large_array(self):
        """Test with large array."""
        size = 10000
        arr = [1] * size
        ft = FenwickTree(size)
        ft.build_from_array(arr)
        
        # Sum of first 100 elements = 100
        assert ft.query(99) == 100, "Large array query failed"
        
        # Sum of all elements = 10000
        assert ft.query(size - 1) == size, "Large array full query failed"
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Single element
        ft = FenwickTree(1)
        ft.update(0, 5)
        assert ft.query(0) == 5, "Single element failed"
        
        # All zeros
        ft_zero = FenwickTree(5)
        assert ft_zero.query(4) == 0, "All zeros failed"
        
        # Build empty then update
        ft_empty = FenwickTree(3)
        ft_empty.update(0, 1)
        ft_empty.update(1, 2)
        ft_empty.update(2, 3)
        assert ft_empty.query(2) == 6, "Build from empty failed"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])