class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = list(s)
        for c in t:
            if c not in st:
                return c
            else:
                st.remove(c)
                
        