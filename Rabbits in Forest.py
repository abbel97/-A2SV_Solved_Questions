class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        for answer in answers:
            count[answer] = count.get(answer, 0) + 1
        total = 0
        for answer, freq in count.items():
            if answer == 0:
                total += freq
            else:
                groups = (freq + answer) // (answer + 1)
                total += groups * (answer + 1)
        return total