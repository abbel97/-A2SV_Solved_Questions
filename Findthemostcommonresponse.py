class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter(word for r in responses for word in set(r))
        max_freq = max(count.values())
        return min(word for word, freq in count.items() if freq == max_freq)