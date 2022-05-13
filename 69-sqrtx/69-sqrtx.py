class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 1, x
        res = 0
        
        while start <= end:
            mid = (start+end) // 2
            square = mid * mid
            
            if square == x:
                return mid
            
            elif square < x:
                start = mid + 1
                res = mid
                
            else:
                end = mid -1
                
        return res