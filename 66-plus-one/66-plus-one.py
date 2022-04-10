class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''.join(map(str, digits))
        m = int(n) + 1
        res = []
        for i in str(m):
            res.append(i)
        return res
        #for i in range(len(digits)-1, 0):
            