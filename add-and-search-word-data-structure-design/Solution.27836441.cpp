struct TrieNode {
    
    TrieNode()
        : WordEnd(false)
    {
    }
    
    bool WordEnd;
    array<unique_ptr<TrieNode>, 26> Edges;
};

class WordDictionary {
public:

    // Adds a word into the data structure.
    void addWord(string word) {
        TrieNode* current = &Root;
        for (char letter : word)
        {
            auto& next = current->Edges[letter - 'a'];
            if (!next)
            {
                next = unique_ptr<TrieNode>(new TrieNode());
            }
            
            current = next.get();
        }
        
        current->WordEnd = true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    bool search(string word) {
        return search(&Root, word, 0);
    }
    
private:

    static bool search(TrieNode* root, const string& word, size_t index)
    {
        TrieNode* current = root;
        
        while ((index < word.length()) && (word[index] != '.'))
        {
            char c = word[index];
            auto& next = current->Edges[c - 'a'];
            if (!next)
            {
                return false;
            }
            
            current = next.get();
            ++index;
        }

        if (index == word.length())
        {
            return current->WordEnd;
        }
        
        // word[index] == '.'
        
        for (auto& next : current->Edges)
        {
            if (!next)
            {
                continue;
            }
            
            if (search(next.get(), word, index + 1))
            {
                return true;
            }
        }
        
        return false;
    }

    TrieNode Root;
};

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary;
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");