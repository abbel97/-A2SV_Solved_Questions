class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            needed_day = 1
            current_weight = 0

            for w in weights:
                if current_weight+w > capacity:
                    needed_day += 1
                    current_weight = w
                else:
                    current_weight += w
            return needed_day <= days

        l = max(weights)
        r = sum(weights)
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans