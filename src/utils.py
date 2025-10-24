"""
Utility Functions for Data Generation and Benchmarking
======================================================

Helper functions for testing and performance analysis.

"""

import random
import string
import time
from typing import List


class DataGenerator:
    """Generate synthetic datasets for benchmarking."""
    
    @staticmethod
    def generate_words(count: int, min_len: int = 3, max_len: int = 10) -> List[str]:
        """
        Generate random words.
        
        Args:
            count (int): Number of words
            min_len (int): Minimum word length
            max_len (int): Maximum word length
            
        Returns:
            List[str]: List of random words
        """
        words = []
        for _ in range(count):
            length = random.randint(min_len, max_len)
            word = ''.join(random.choices(string.ascii_lowercase, k=length))
            words.append(word)
        return words
    
    @staticmethod
    def generate_integers(count: int, max_val: int = 1000000) -> List[int]:
        """
        Generate random integers.
        
        Args:
            count (int): Number of integers
            max_val (int): Maximum value
            
        Returns:
            List[int]: List of random integers
        """
        return [random.randint(0, max_val) for _ in range(count)]
    
    @staticmethod
    def generate_array(count: int, max_val: int = 100) -> List[int]:
        """
        Generate array for Fenwick Tree.
        
        Args:
            count (int): Array size
            max_val (int): Maximum value
            
        Returns:
            List[int]: Array of values
        """
        return [random.randint(1, max_val) for _ in range(count)]