"""
Unit Tests for Trie Data Structure
===================================

Run with: python -m pytest tests/test_trie.py -v
Or directly: python tests/test_trie.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src.trie import Trie


class TestTrie:
    """Comprehensive Trie tests."""
    
    def test_basic_insert_search(self):
        """Test basic insert and search operations."""
        trie = Trie()
        words = ["cat", "car", "card", "care", "careful"]
        
        for word in words:
            trie.insert(word)
        
        # Test search
        for word in words:
            assert trie.search(word), f"Failed to find '{word}'"
        
        # Test non-existent words
        assert not trie.search("ca"), "Found incomplete word 'ca'"
        assert not trie.search("cards"), "Found non-existent word 'cards'"
    
    def test_prefix_search(self):
        """Test prefix search functionality."""
        trie = Trie()
        words = ["apple", "app", "application", "apply"]
        
        for word in words:
            trie.insert(word)
        
        assert trie.starts_with("app"), "Failed prefix 'app'"
        assert trie.starts_with("appl"), "Failed prefix 'appl'"
        assert not trie.starts_with("orange"), "Found non-existent prefix 'orange'"
    
    def test_delete_operations(self):
        """Test delete operations."""
        trie = Trie()
        words = ["test", "testing", "tester"]
        
        for word in words:
            trie.insert(word)
        
        # Delete one word
        assert trie.delete("test"), "Delete failed"
        assert not trie.search("test"), "Deleted word still found"
        assert trie.search("testing"), "Delete affected other words"
        
        # Try to delete non-existent word
        assert not trie.delete("nonexistent"), "Delete of non-existent word should return False"
    
    def test_edge_cases(self):
        """Test edge cases."""
        trie = Trie()
        
        # Empty string
        trie.insert("")
        assert trie.search(""), "Failed to handle empty string"
        
        # Single character
        trie.insert("a")
        assert trie.search("a"), "Failed single character"
        
        # Very long word
        long_word = "a" * 100
        trie.insert(long_word)
        assert trie.search(long_word), "Failed very long word"
    
    def test_duplicate_inserts(self):
        """Test duplicate insertions."""
        trie = Trie()
        
        trie.insert("test")
        initial_count = trie.word_count
        trie.insert("test")  # Duplicate
        
        assert trie.word_count == initial_count, "Word count increased on duplicate"
        assert trie.search("test"), "Word not found after duplicate insert"
    
    def test_case_sensitivity(self):
        """Test case sensitivity."""
        trie = Trie()
        
        trie.insert("Test")
        trie.insert("test")
        
        assert trie.search("Test"), "Failed to find 'Test'"
        assert trie.search("test"), "Failed to find 'test'"
        assert trie.word_count == 2, "Should count different cases separately"


if __name__ == "__main__":
    # This allows running the test file directly
    pytest.main([__file__, "-v"])