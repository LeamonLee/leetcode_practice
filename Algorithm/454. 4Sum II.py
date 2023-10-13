class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dctMap = {}
        res=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                twoSum = nums1[i]+nums2[j]
                if twoSum not in dctMap:
                    dctMap[twoSum] = 1
                else:
                    dctMap[twoSum] += 1
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                twoSum = nums3[i]+nums4[j]
                res += dctMap.get(-1*twoSum , 0)
    
        return res