class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum_soFar = 0
        prefix_sum_count = {0: 1} 

        for num in nums:
            sum_soFar += num
            
            if (sum_soFar - goal) in prefix_sum_count:
                count += prefix_sum_count[sum_soFar - goal]
            
            if sum_soFar in prefix_sum_count:
                prefix_sum_count[sum_soFar] += 1
            else:
                prefix_sum_count[sum_soFar] = 1
        return count