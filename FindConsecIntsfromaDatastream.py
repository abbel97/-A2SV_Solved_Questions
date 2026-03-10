from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        
    def consec(self, num: int) -> bool:
        if len(self.q) == self.k:
            self.q.popleft()
        if num == self.value:
            self.q.append(num)
        else:
            self.q.clear()
        return len(self.q) == self.k

