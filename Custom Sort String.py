class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_index = {char: i for i, char in enumerate(order)}
        sorted_s = sorted(s, key=lambda x: order_index.get(x, float('inf')))
        
        return ''.join(sorted_s)