class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for key, val in enumerate(s):
            if d[val] == 1:
                return key
        return -1
            
        