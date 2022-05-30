class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber
        
        while n > 0:
            c = chr(ord('A') + (n-1) % 26)
            res = c + res
            n = (n-1) // 26
            
        return res
        