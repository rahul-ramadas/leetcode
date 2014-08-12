class Solution {
public:

    bool findWord(const vector<vector<char>>& board, int row, int col, const string& word, size_t ind, vector<vector<bool>>& visited)
    {
        if (visited[row][col])
        {
            return false;
        }

        if (board[row][col] != word[ind])
        {
            return false;
        }
        
        if (ind == (word.size() - 1))
        {
            return true;
        }
        
        visited[row][col] = true;
        
        static int rowOffs[] = { -1, 1, 0, 0 };
        static int colOffs[] = { 0, 0, -1, 1 };
        
        bool found = false;
        for (int i = 0; i < 4 && !found; ++i)
        {
            int newRow = row + rowOffs[i];
            int newCol = col + colOffs[i];
            if (newRow < 0 || newRow >= board.size())
            {
                continue;
            }
            if (newCol < 0 || newCol >= board[newRow].size())
            {
                continue;
            }
            
            found = findWord(board, newRow, newCol, word, ind + 1, visited);
        }
        
        visited[row][col] = false;
        return found;
    }

    bool exist(vector<vector<char> > &board, string word) {
        if (board.empty())
        {
            return word.empty();
        }

        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        for (int row = 0; row < (int)board.size(); ++row)
        {
            for (int col = 0; col < (int)board[row].size(); ++col)
            {
                if (findWord(board, row, col, word, 0, visited))
                {
                    return true;
                }
            }
        }
        
        return false;
    }
};
