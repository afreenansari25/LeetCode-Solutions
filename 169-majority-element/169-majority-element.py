class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashT = {}
        maxV = 0
        
        for num in nums:
            if num not in hashT:
                hashT[num] = 1
            else:
                hashT[num] += 1
            maxV = max(maxV, hashT[num])
        #for key, value in hashT.items():
            
            
        for key, value in hashT.items():
            if value == maxV:
                return key
        