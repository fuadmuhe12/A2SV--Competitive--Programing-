class Double:
    def __init__(self, page):
        self.page = page
        self.ford = None
        self.back = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Double(homepage)
        

    def visit(self, url: str) -> None:
        page = Double(url)
        self.cur.ford = page
        page.back = self.cur
        self.cur = page
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.back:
            self.cur = self.cur.back
            steps -= 1

        return self.cur.page

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.ford:
            self.cur = self.cur.ford
            steps -= 1

        return self.cur.page

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)