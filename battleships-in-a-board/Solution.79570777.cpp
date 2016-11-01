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

    int countBattleships(vector<vector<char>>& board)
    {
        int count = 0;

        for (int row = 0; row < (int) board.size(); ++row)
        {
            for (int col = 0; col < (int) board[row].size(); ++ col)
            {
                if (board[row][col] == '.')
                {
                    continue;
                }

                if (!isShipPiece(board, row, col - 1) && !isShipPiece(board, row - 1, col))
                {
                    ++count;
                }
            }
        }

        return count;
    }
};
