struct TrieNode {
    TrieNode ()
        : IsWordEnd(false), FoundAlready(false)
    {
    }
    
    array<unique_ptr<TrieNode>, 26> Edges;
    bool IsWordEnd;
    bool FoundAlready;
};

class Solution {
public:

    unique_ptr<TrieNode> buildTrie(const vector<string>& words)
    {
        unique_ptr<TrieNode> root(new TrieNode());
        
        for (auto& word: words)
        {
            TrieNode* nextNode = root.get();
            for (auto c: word)
            {
                auto& nextEdge = nextNode->Edges[c - 'a'];
                if (!nextEdge)
                {
                    nextEdge.reset(new TrieNode());
                }
                nextNode = nextEdge.get();
            }
            
            nextNode->IsWordEnd = true;
        }
        
        return root;
    }
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        auto root = buildTrie(words);
        vector<string> solution;
        
        for (size_t i = 0; i < board.size(); ++i)
        {
            for (size_t j = 0; j < board[i].size(); ++j)
            {
                unordered_set<size_t> visited;
                string currentWord;
                search_trie(root.get(), i, j, board, visited, solution, currentWord);
            }
        }
        
        return solution;
    }
    
    void search_trie(TrieNode* Root, int I, int J, vector<vector<char>>& Board, unordered_set<size_t>& Visited, vector<string>& Solution, string& CurrentWord)
    {
        size_t N = Board.size();
        size_t M = Board[0].size();
        size_t index = I * M + J;
        if (I < 0 || I >= N || J < 0 || J >= M)
        {
            return;
        }
        
        char c = Board[I][J];

        auto& nextNode = Root->Edges[c - 'a'];
        if (!nextNode)
        {
            return;
        }
        
        if (Visited.count(index) != 0)
        {
            return;
        }
        
        Visited.insert(index);
        CurrentWord += c;
        
        if (nextNode->IsWordEnd && !nextNode->FoundAlready)
        {
            Solution.push_back(CurrentWord);
            nextNode->FoundAlready = true;
        }
        
        search_trie(nextNode.get(), I - 1, J, Board, Visited, Solution, CurrentWord);
        search_trie(nextNode.get(), I, J - 1, Board, Visited, Solution, CurrentWord);
        search_trie(nextNode.get(), I, J + 1, Board, Visited, Solution, CurrentWord);
        search_trie(nextNode.get(), I + 1, J, Board, Visited, Solution, CurrentWord);
        
        CurrentWord.pop_back();
        Visited.erase(index);
    }
};
