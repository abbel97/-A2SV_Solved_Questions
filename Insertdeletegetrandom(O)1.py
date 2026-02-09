class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        xy = self.pos[val]
        last_element = self.nums[-1]
        self.nums[xy] = last_element
        self.pos[last_element] = xy
        self.nums.pop()
        del self.pos[val]
        return True
        

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums)