class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        sum = num // 3
        return [sum-1, sum, sum+1]

        