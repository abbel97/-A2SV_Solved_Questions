class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        
        for start, end in requests:
            count[start] += 1
            if end + 1 < n:
                count[end + 1] -= 1
        
        for i in range(1, n):
            count[i] += count[i - 1]
        
        count.pop()  
        nums.sort()
        count.sort()
        
        total_sum = 0
        for i in range(n):
            total_sum += nums[i] * count[i]
        
        return total_sum % (10**9 + 7)