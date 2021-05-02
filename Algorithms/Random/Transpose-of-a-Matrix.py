class Solution:
    def solve(self, matrix):
        t = []
        for r in range(len(matrix)):
            temp = []
            for c in range(len(matrix[r])):
                temp.append(matrix[c][r])
            t.append(temp)
        return t
