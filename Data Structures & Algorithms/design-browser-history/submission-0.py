class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.currentPos = 0
        self.history = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:

        checker = len(self.history)

        for i in range (self.currentPos + 1, checker, 1):
            self.history.pop()

        self.history.append(url)
        self.currentPos = len(self.history) - 1
        

    def back(self, steps: int) -> str:

        if steps > self.currentPos:
            self.currentPos = 0
            return self.history[0]
        else:
            self.currentPos = self.currentPos - steps
            return self.history[self.currentPos]
        

    def forward(self, steps: int) -> str:
        if(steps + self.currentPos >= len(self.history)):
            self.currentPos = len(self.history)-1
            return self.history[self.currentPos]
        else:
            self.currentPos = self.currentPos + steps
            return self.history[self.currentPos]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)