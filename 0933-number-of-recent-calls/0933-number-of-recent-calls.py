class RecentCounter:

    def __init__(self):
        self.q = []
        self.rc = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.rc += 1

        while self.q[0] < (t-3000):
            self.q.pop(0)
            self.rc -= 1
        
        return self.rc


