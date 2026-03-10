class RecentCounter:

    def __init__(self):
        self.q = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[-1] - self.q[0] > 3000:
            self.q.pop(0)
        return len(self.q) - self.start
        