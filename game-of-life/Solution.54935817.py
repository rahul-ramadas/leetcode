class Solution:

    def gameOfLife(self, board):
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                live_neighbors = self.count_live_neighbors(board, i, j)

                if board[i][j] & 0x1:
                    if 2 <= live_neighbors <= 3:
                        board[i][j] |= 0x2
                else:
                    if live_neighbors == 3:
                        board[i][j] |= 0x2

        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                board[i][j] >>= 1


    def count_live_neighbors(self, board, x, y):
        live_count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue

                xp = x + i
                yp = y + j

                if xp < 0 or xp >= len(board):
                    continue

                if yp < 0 or yp >= len(board[xp]):
                    continue

                live_count += board[xp][yp] & 0x1

        return live_count
