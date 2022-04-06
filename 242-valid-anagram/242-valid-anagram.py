from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' 
        # solution 1
        if Counter(s) == Counter(t):
            return True
        return False
        
        #solution 2
        if sorted(s) == sorted(t):
            return True
        return False
        '''
        countS, countT = {},{}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for key in countS:
            if countS[key] != countT.get(key,0):
                return False
        return True
        
        
        
        
                