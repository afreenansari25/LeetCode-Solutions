class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = [i for i in magazine]
        
        for c in ransomNote:
            if c in m:
                m.remove(c)
            else:
                return False
        return True
        