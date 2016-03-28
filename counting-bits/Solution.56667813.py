class Solution:

    def countBits(self, num):
        if num == 0:
            return [0]

        result = [0]

        while len(result) < (num + 1):
            remaining = min(num + 1 - len(result), len(result))
            result.extend([c + 1 for c in result[:remaining]])

        return result[:num + 1]
