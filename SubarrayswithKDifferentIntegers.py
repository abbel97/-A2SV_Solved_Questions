class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def mostK(nums, k):
            count = {}
            res = left = 0
            
            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1
                
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                res += right - left + 1
            return res
        
        return mostK(nums, k) - mostK(nums, k - 1)