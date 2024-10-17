class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            if sorted(matrix[i]) != list(range(1, n + 1)):
                return False
        
        for j in range(n):
            column = [matrix[i][j] for i in range(n)]
            if sorted(column) != list(range(1, n + 1)):
                return False
        return True
