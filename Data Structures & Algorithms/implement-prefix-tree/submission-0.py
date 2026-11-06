class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        # Every Trie starts with an empty root node
        self.root = TrieNode()     

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If the character isn't a child of the current node, create it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move down into that child node
            curr = curr.children[char]
        # Once the loop finishes, mark the last node as the end of a word
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # If a character is missing, the word definitely doesn't exist
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Return True ONLY if this node marks the end of a full word    
        return curr.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # For a prefix, we don't care if it's a full word. 
        # If we successfully traced the characters, return True
        return True

        
        