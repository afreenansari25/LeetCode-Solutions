class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, count = 0, 0
        
        for r, num in enumerate(nums):
            if num == 0:
                l = r + 1
            count = max(count, r-l+1)
        return count
    
        ''' 
        windowSize, newCount, p = [], 0, 0
        
        for i in range(len(nums)+1):            
            if i == len(nums) or nums[i] == 0:
                windowSize.append(newCount)
                newCount = 0
            elif nums[i] == 1:
                newCount += 1
                
        return max(windowSize)
        '''
        