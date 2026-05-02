class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        for i in range(1, n+1):
            s.add(i)
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                dup = i
        return [dup, s.pop()]