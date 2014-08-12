class Solution {
public:

    bool floodfill(vector<vector<char>>& board, int i, int j, vector<vector<bool>>& visited, bool change)
    {
        vector<vector<bool>> trialVisited = visited;
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));
        trialVisited[i][j] = true;
        bool surrounded = true;
        array<int, 4> xs = { -1, 0, 0, 1 };
        array<int, 4> ys = { 0, -1, 1, 0 };

        while (!q.empty())
        {
            auto point = q.front();
            q.pop();

            if (change)
            {
                board[point.first][point.second] = 'X';
            }

            for (size_t i = 0; i < xs.size(); ++i)
            {
                int x = point.first + xs[i];
                int y = point.second + ys[i];

                if (x < 0 || x >= (int)board.size())
                {
                    surrounded = false;
                    continue;
                }

                if (y < 0 || y >= (int)board[x].size())
                {
                    surrounded = false;
                    continue;
                }

                if (board[x][y] == 'X')
                {
                    continue;
                }

                if (trialVisited[x][y])
                {
                    continue;
                }

                trialVisited[x][y] = true;
                q.push(make_pair(x, y));
            }
        }

        if (change || !surrounded)
        {
            visited = std::move(trialVisited);
        }

        return surrounded;
    }

    void solve(vector<vector<char>> &board) {
        if (board.empty())
        {
            return;
        }

        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));

        for (int i = 0; i < (int)board.size(); ++i)
        {
            for (int j = 0; j < (int)board[i].size(); ++j)
            {
                if (visited[i][j])
                {
                    continue;
                }

                if (board[i][j] != 'O')
                {
                    continue;
                }

                if (floodfill(board, i, j, visited, false))
                {
                    floodfill(board, i, j, visited, true);
                }
            }
        }
    }
};
