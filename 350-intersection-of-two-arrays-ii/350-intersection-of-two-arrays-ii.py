class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        p1, p2, res = 0, 0, []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1, p2 = p1 + 1, p2 + 1
            else:
                p1 += 1
        return res
        '''
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res        
        