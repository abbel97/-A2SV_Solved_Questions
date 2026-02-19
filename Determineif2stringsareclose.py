class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False 
        frequency1 = defaultdict(int)
        frequency2 = defaultdict(int)

        for char in word1:
            frequency1[char] += 1
        for char in word2:
            frequency2[char] += 1
        
        if set(frequency1.keys()) != set(frequency2.keys()):
            return False 
        sorted_freq1 = sorted(frequency1.values())
        sorted_freq2 = sorted(frequency2.values())

        return sorted_freq1 == sorted_freq2