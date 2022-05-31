class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = list(magazine)
        
        for c in ransomNote:
            if c in m:
                m.remove(c)
            else:
                return False
        return True
        