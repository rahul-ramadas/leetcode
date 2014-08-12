class Solution:

    def isValidSudoku(self, board):

        def contains_repeated_digits(list_of_elements):
            set_of_digits = set()
            for elem in list_of_elements:
                if not str.isdigit(elem):
                    continue
                if elem in set_of_digits:
                    return True
                set_of_digits.add(elem)
            return False

        for row in board:
            if contains_repeated_digits(row):
                return False

        for col in itertools.izip(*board):
            if contains_repeated_digits(col):
                return False

        for box_row in xrange(3):
            for box_col in xrange(3):
                elements = [board[x][y] for x in xrange(box_row*3, box_row*3 + 3) for y in xrange(box_col*3, box_col*3 + 3)]
                if contains_repeated_digits(elements):
                    return False

        return True
