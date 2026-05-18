class Solution:
        def splitString(self, s: str) -> bool: 
            def backtrack(start, prev):
                if start == len(s):
                    return True
                
                for end in range(start + 1, len(s) + 1):
                    num_str = s[start:end]
                    num = int(num_str)
                    
                    if prev is not None and num >= prev:
                        continue
                    if backtrack(end, num):
                        return True
                return False
            return backtrack(0, None)