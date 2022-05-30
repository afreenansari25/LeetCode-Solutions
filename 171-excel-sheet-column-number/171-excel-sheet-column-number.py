class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        
        for c in s:
            d = ord(c) - ord('A') + 1 
            res = res*26 + d
            
        return res
            
            
        