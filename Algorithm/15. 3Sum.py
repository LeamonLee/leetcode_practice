'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=list()
        nums.sort() # 這一步很重要!
        '''
        -1,0,1,2,-1,-4
        i  l         r
        '''
        for i in range(len(nums)-2):
            # 如果i和上一個用的一樣就換下一個
            if i > 0 and nums[i-1] == nums[i]: continue
            
            l = i+1
            r = len(nums)-1

            while l<r:
                # print(f"len(nums):{len(nums)}, i:{i}, l:{l}, r:{r}")
                threeSum = nums[i]+nums[l]+nums[r]
                # if threeSum == 0 and [nums[i], nums[l], nums[r]] not in res: 
                #     res.append([nums[i], nums[l], nums[r]])
                if threeSum == 0: 
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    while l < r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1

                elif threeSum > 0:
                    r-=1
                else:
                    l+=1
        
        return res