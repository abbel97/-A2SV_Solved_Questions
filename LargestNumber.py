class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        intToString = list(map(str, nums))
        
        intToString.sort(key=lambda x: x*10, reverse=True)
        largestNum = ''.join(intToString)
        return '0' if largestNum[0] == '0' else largestNum