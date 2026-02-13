class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_map = {}
        count = 0

        for i, num in enumerate(nums):
            if num in index_map:
                for j in index_map[num]:
                    if (i * j) % k == 0:
                        count += 1
                index_map[num].append(i)
            else:
                index_map[num] = [i]
        return count
