class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gc, sc = 0, 0
        count = 0
        while gc < len(g) and sc < len(s):
            if s[sc] >= g[gc]:
                count += 1
                gc, sc = gc + 1, sc + 1
            else:
                sc += 1
        return count
        