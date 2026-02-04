#Geeks for Geeks


class Solution:
    def findUnion(self, a, b,):
        union_set = set()
        
        for num in a:
            union_set.add(num)
        
        for num in b:
            union_set.add(num)
        
        return list(union_set)
    