import random

class SkipNode:
    """
    Node class for Skip list.
    
    Attributes:
        key: The value stored in the node
        forward: list of forward pointers at each level
    """
    def __init__(self, key: int, level: int):
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList:
    """
    Skip list implementation - probabilistic alternative to balanced trees.
    
    Time Complexity:
        - Insert: O(log n) average, O(n) worst case
        - Search: O(log n) average, O(n) worst case
        - Delete: O(log n) average, O(n) worst case
    
    Space Complexity: O(n)
    
    Use Case: Database indexing, in-memory data stores (Redis uses skip lists),
             alternative to balanced BSTs with simpler implementation
    """
    
    def __init__(self, max_level: int = 16, p: float = 0.5):
        """
        Initialize empty Skip list.
        
        Input: max_level (int) - maximum number of levels
               p (float) - probability for level generation (typically 0.5)
        Output: None
        
        Explanation: Creates header node with maximum possible height.
        Probability p determines average height (0.5 gives expected height of log2(n)).
        """
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(float('-inf'), max_level)
        self.level = 0  # Current maximum level in use
        self.size = 0
    
    def _random_level(self) -> int:
        """
        Generate random level for new node.
        
        Input: None
        Output: int - random level between 0 and max_level
        
        Explanation: Uses geometric distribution with probability p.
        Each level has p chance of going one level higher.
        """
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def insert(self, key: int) -> None:
        """
        Insert a key into the Skip list.
        
        Input: key (int) - value to insert
        Output: None
        
        Explanation: Finds insertion position at each level, creates new node
        with random height, and updates forward pointers.
        """
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find position to insert at each level
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        # Generate random level for new node
        new_level = self._random_level()
        
        # Update list level if necessary
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level
        
        # Create new node and update pointers
        new_node = SkipNode(key, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
        
        self.size += 1
    
    def search(self, key: int) -> bool:
        """
        Search for a key in the Skip list.
        
        Input: key (int) - value to search for
        Output: bool - True if found, False otherwise
        
        Explanation: Starts from highest level, moves forward while key is greater,
        then drops down a level. Repeats until key is found or bottom is reached.
        """
        current = self.header
        
        # Traverse from top level to bottom
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        
        # Move to next node at level 0
        current = current.forward[0]
        
        # Check if we found the key
        return current is not None and current.key == key
    
    def delete(self, key: int) -> bool:
        """
        Delete a key from the Skip list.
        
        Input: key (int) - value to delete
        Output: bool - True if deleted, False if not found
        
        Explanation: Finds the node at each level, updates pointers to bypass it,
        then removes the node.
        """
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find node to delete at each level
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If key not found
        if current is None or current.key != key:
            return False
        
        # Update forward pointers to skip the deleted node
        for i in range(self.level + 1):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]
        
        # Update list level
        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1
        
        self.size -= 1
        return True
