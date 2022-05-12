class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        oldString = strs[0]
        
        for i in range(1, len(strs)):          
            newString = strs[i]
            
            while newString[:len(oldString)] != oldString:
                oldString = oldString[:len(oldString)-1]
                
                if len(oldString) == 0:
                    return ""
                
        return oldString
                
        