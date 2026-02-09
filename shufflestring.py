class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for i, index in enumerate(indices):
            result[index] = s[i]
        return ''.join(result)
        