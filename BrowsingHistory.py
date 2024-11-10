class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.cur = 0
        

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.cur + 1]
        self.hist.append(url)
        self.cur += 1
        

    def back(self, steps: int) -> str:
        self.cur = self.cur-steps if (self.cur-steps)>0 else 0
        return self.hist[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = self.cur+steps if (self.cur+steps) < len(self.hist) else len(self.hist)-1
        return self.hist[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)