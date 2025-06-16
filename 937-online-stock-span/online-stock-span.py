class StockSpanner(object):
    def __init__(self):
        self.st = []

    def next(self, price):
        span = 1
        while self.st and self.st[-1][0] <= price:
            span += self.st.pop()[1]
        self.st.append((price, span))
        return span