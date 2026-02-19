class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_array = sorted(nums)
        new_arr = []
        for element in nums:
            count = sorted_array.index(element)
            new_arr.append(count)
        return new_arr
