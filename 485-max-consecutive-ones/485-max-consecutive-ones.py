class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        windowSize, newCount = [], 0
        for i in range(len(nums)+1):            
            if i == len(nums) or nums[i] == 0:
                windowSize.append(newCount)
                newCount = 0
            elif nums[i] == 1:
                newCount += 1
        print(windowSize)
        return max(windowSize)
        