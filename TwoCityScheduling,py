class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[1] - x[0]))

        l = 0
        r = len(costs) - 1

        res = 0
        while l<r:
            ab = costs[l][0] + costs[r][1]
            ba = costs[l][1] + costs[r][0]

            l += 1
            r -= 1
            res += min(ab, ba)
        return res

            