class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.l = len(grid)

    def getIndOfVal(self, value):
        row = col = 0
        for i in range(self.l):
            if value in self.grid[i]:
                row = i
                col = self.grid[i].index(value)
                return row, col

    def adjacentSum(self, value: int) -> int:
        row, col = self.getIndOfVal(value)
        s = 0
        if row+1 != self.l:
            s += self.grid[row+1][col]
        if row-1 != -1:
            s += self.grid[row-1][col]
        if col-1 != -1:
            s += self.grid[row][col-1]
        if col+1 != self.l:
            s += self.grid[row][col+1]

        return s
        

    def diagonalSum(self, value: int) -> int:
        row, col = self.getIndOfVal(value)
        s = 0
        if row+1 != self.l and col+1 != self.l:
            s += self.grid[row+1][col+1]
        if row+1 != self.l and col-1 != -1:
            s += self.grid[row+1][col-1]
        if row-1 != -1 and col+1 != self.l:
            s += self.grid[row-1][col+1]
        if row-1 != -1 and col-1 != -1:
            s += self.grid[row-1][col-1]

        return s
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)