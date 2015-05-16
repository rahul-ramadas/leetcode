class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.edges = dict()
        self.word_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        
        for c in word:
            next_elem = current.edges.get(c)
            if next_elem is None:
                next_elem = TrieNode()
                current.edges[c] = next_elem
            current = next_elem
            
        current.word_end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        end_node = self.traverse(word)
        if end_node is None:
            return False
        return end_node.word_end

    def traverse(self, word):
        current = self.root
        
        for c in word:
            next_elem = current.edges.get(c)
            if next_elem is None:
                return None
            current = next_elem
            
        return current

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        end_node = self.traverse(prefix)
        if end_node is None:
            return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
