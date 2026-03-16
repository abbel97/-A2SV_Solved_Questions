class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        prefix_sum_map = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0: 
                prefix_sum_mod = prefix_sum % k
            else:
                prefix_sum_mod = prefix_sum
            
            if prefix_sum_mod in prefix_sum_map:
                if i - prefix_sum_map[prefix_sum_mod] > 1: 
                    return True
            else:
                prefix_sum_map[prefix_sum_mod] = i
        return False