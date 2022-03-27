class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for key, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return key, seen[remaining]
            seen[value] = key
            
        