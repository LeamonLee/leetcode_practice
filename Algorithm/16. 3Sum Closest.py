'''
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff=float("inf")
        res=0
        nums.sort() # 關鍵一步
        
        '''
        -1,0,1,2,-1,-4
        i  l         r
        '''
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l=i+1
            r=len(nums)-1

            while l < r:
                threeSum = nums[i]+nums[l]+nums[r]
                _diff = abs(threeSum-target)
                if _diff < diff:
                    # print(f"i:{nums[i]}, l:{nums[l]}, r:{nums[r]}, threeSum:{threeSum}, diff:{diff}, target:{target}")
                    diff = _diff
                    res=threeSum

                if threeSum == target:
                    return target
                elif threeSum > target:
                    r-=1
                elif threeSum < target:
                    l+=1
        
        return res