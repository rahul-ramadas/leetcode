class Solution
{
public:

    bool isShipPiece(const vector<vector<char>>& board, int row, int col)
    {
        int rows = (int)board.size();
        int cols = (int)board[0].size();

        if ((row >= rows) || (row < 0) || (col >= cols) || (col < 0))
        {
            return false;
        }

        return board[row][col] == 'X';
    }

    bool isHorizontalBattleship(const vector<vector<char>>& board, int row, int col)
    {
        return isShipPiece(board, row, col - 1) || isShipPiece(board, row, col + 1);
    }

    bool isVerticalBattleship(const vector<vector<char>>& board, int row, int col)
    {
        return !isHorizontalBattleship(board, row, col);
    }

    int countBattleships(vector<vector<char>>& board)
    {
        int count = 0;

        for (int row = 0; row < (int) board.size(); ++row)
        {
            int lastEnd = -2;

            for (int col = 0; col < (int) board[row].size(); ++ col)
            {
                if (board[row][col] == '.')
                {
                    continue;
                }

                if (!isHorizontalBattleship(board, row, col))
                {
                    continue;
                }

                if (col != (lastEnd + 1))
                {
                    ++count;
                }

                lastEnd = col;
            }
        }

        for (int col = 0; col < (int)board[0].size(); ++col)
        {
            int lastEnd = -2;

            for (int row = 0; row < (int)board.size(); ++row)
            {
                if (board[row][col] == '.')
                {
                    continue;
                }

                if (!isVerticalBattleship(board, row, col))
                {
                    continue;
                }

                if (row != (lastEnd + 1))
                {
                    ++count;
                }

                lastEnd = row;
            }
        }

        return count;
    }
};
