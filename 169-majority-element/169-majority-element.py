class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashT = {}
        maxV = 0
        
        for num in nums:
            if num not in hashT:
                hashT[num] = 1
            else:
                hashT[num] += 1
        
        for key, value in hashT.items():
            maxV = max(maxV, hashT[key])
            
        for key, value in hashT.items():
            if value == maxV:
                return key
        