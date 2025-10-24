class TrieNode:
    """
    Node class for Trie data structure.
    
    Attributes:
        children: Dictionary mapping characters to child nodes
        is_end: Boolean indicating if this node marks the end of a word
    """
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    Trie (Prefix Tree) implementation for efficient string operations.
    
    Time Complexity:
        - Insert: O(m) where m is the length of the word
        - Search: O(m)
        - StartsWith: O(m)
        - Delete: O(m)
    
    Space Complexity: O(ALPHABET_SIZE * N * M)
        In practice: O(total characters across all words)
    
    Use Case: Autocomplete systems, spell checkers, IP routing tables
    """
    
    def __init__(self):
        """Initialize empty Trie with root node."""
        self.root = TrieNode()
        self.word_count = 0
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        
        Input: word (str) - the word to insert
        Output: None
        
        Explanation: Traverses the Trie, creating nodes as needed for each character.
        Marks the last node as end of word.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        if not node.is_end:
            node.is_end = True
            self.word_count += 1
    
    def search(self, word: str) -> bool:
        """
        Search for an exact word in the Trie.
        
        Input: word (str) - the word to search for
        Output: bool - True if word exists, False otherwise
        
        Explanation: Traverses the Trie following the characters of the word.
        Returns True only if path exists and ends at a word-end node.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.
        
        Input: prefix (str) - the prefix to search for
        Output: bool - True if prefix exists, False otherwise
        
        Explanation: Traverses the Trie following the prefix characters.
        Returns True if the path exists, regardless of word-end markers.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the Trie.
        
        Input: word (str) - the word to delete
        Output: bool - True if word was deleted, False if not found
        
        Explanation: Marks the end-of-word flag as False. Does not remove nodes
        to maintain other words sharing the same prefix.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        if node.is_end:
            node.is_end = False
            self.word_count -= 1
            return True
        return False
    
    def get_all_words_with_prefix(self, prefix: str) -> list[str]:
        """
        Get all words that start with the given prefix.
        
        Input: prefix (str) - the prefix to match
        Output: list[str] - list of all matching words
        
        Explanation: Finds the prefix node, then performs DFS to collect all words.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._dfs_collect(node, prefix, results)
        return results
    
    def _dfs_collect(self, node: TrieNode, current_word: str, results: list[str]) -> None:
        """
        Helper method for DFS traversal to collect words.
        
        Input: node (TrieNode), current_word (str), results (list[str])
        Output: None (modifies results list in-place)
        """
        if node.is_end:
            results.append(current_word)
        
        for char, child_node in node.children.items():
            self._dfs_collect(child_node, current_word + char, results)