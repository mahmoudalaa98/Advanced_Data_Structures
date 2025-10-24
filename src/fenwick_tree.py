class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) for efficient prefix sum queries and updates.
    
    Time Complexity:
        - Update: O(log n)
        - Query (prefix sum): O(log n)
        - Range sum: O(log n)
    
    Space Complexity: O(n)
    
    Use Case: Cumulative frequency tables, dynamic range sum queries,
             counting inversions, 2D range queries
    """
    
    def __init__(self, size: int):
        """
        Initialize Fenwick Tree with given size.
        
        Input: size (int) - the size of the array
        Output: None
        
        Explanation: Creates a BIT array of size+1 (1-indexed for easier implementation).
        """
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index: int, delta: int) -> None:
        """
        Update value at index by adding delta.
        
        Input: index (int) - 0-based index to update
               delta (int) - value to add
        Output: None
        
        Explanation: Updates the index and all affected nodes in the tree
        by traversing parent nodes (adding LSB to index).
        """
        index += 1  # Convert to 1-based indexing
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)  # Add LSB
    
    def query(self, index: int) -> int:
        """
        Get prefix sum from index 0 to index (inclusive).
        
        Input: index (int) - 0-based index
        Output: int - sum of elements from 0 to index
        
        Explanation: Sums values by traversing responsible nodes
        (removing LSB from index) until reaching 0.
        """
        index += 1  # Convert to 1-based indexing
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & (-index)  # Remove LSB
        return result
    
    def range_query(self, left: int, right: int) -> int:
        """
        Get sum of elements in range [left, right].
        
        Input: left (int) - left boundary (0-based)
               right (int) - right boundary (0-based, inclusive)
        Output: int - sum of elements in range
        
        Explanation: Uses prefix sum property: range_sum = prefix[right] - prefix[left-1]
        """
        if left > 0:
            return self.query(right) - self.query(left - 1)
        return self.query(right)
    
    def build_from_array(self, arr: list[int]) -> None:
        """
        Build Fenwick Tree from existing array.
        
        Input: arr (list[int]) - array of values
        Output: None
        
        Explanation: Efficiently builds tree by updating each index once.
        """
        for i, val in enumerate(arr):
            self.update(i, val)
