class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        res1, res2 = 0, 0
        for num in nums:
            res1 += num
        for i in range(len(nums)+1):
            res2 += i
        return res2-res1
        '''
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
            
        return res
        