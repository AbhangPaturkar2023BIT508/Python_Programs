class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        state = 0
        while x >= 1 and y >= 4:
            state += 1
            x -= 1
            y -= 4
        if state % 2 == 1:
            return "Alice"
        else:
            return "Bob"