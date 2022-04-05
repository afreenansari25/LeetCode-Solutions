from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' 
        if Counter(s) == Counter(t):
            return True
        return False
        '''
        
        if sorted(s) == sorted(t):
            return True
        return False
        
                