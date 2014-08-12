class Solution:
    def solveNQueens(self, n):
        result = []
        rowAttacked = [False] * n
        colAttacked = [False] * n
        mainDiagAttacked = [False] * (2 * n - 1)
        offDiagAttacked = [False] * (2 * n - 1)
        solution = [['.'] * n for _ in xrange(n)]

        def getMainDiagNumber(row, col):
            return row - col + n - 1

        def getOffDiagNumber(row, col):
            return row + col

        def isAlreadyAttacked(row, col):
            return rowAttacked[row] or \
                colAttacked[col] or \
                mainDiagAttacked[getMainDiagNumber(row, col)] or \
                offDiagAttacked[getOffDiagNumber(row, col)]

        def updateAttacked(row, col, isAttacked=True):
            rowAttacked[row] = isAttacked
            colAttacked[col] = isAttacked
            mainDiagAttacked[getMainDiagNumber(row, col)] = isAttacked
            offDiagAttacked[getOffDiagNumber(row, col)] = isAttacked

        def placeQueen(row):
            if row == n:
                result.append(copy.deepcopy(solution))
                return

            for col in xrange(0, n):
                if isAlreadyAttacked(row, col):
                    continue

                updateAttacked(row, col)
                solution[row][col] = 'Q'
                placeQueen(row + 1)
                solution[row][col] = '.'
                updateAttacked(row, col, False)

        placeQueen(0)
        for i in xrange(0, len(result)):
            for j in xrange(0, len(result[i])):
                result[i][j] = ''.join(result[i][j])
        return result
