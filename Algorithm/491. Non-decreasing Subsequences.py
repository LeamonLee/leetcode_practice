'''
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
'''

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def dfs(startIdx, temp):
            if len(temp)>=2:
                res.append(temp.copy())
            
            visited = set()
            for i in range(startIdx, len(nums)):
                if nums[i] in visited: continue
                if len(temp) == 0 or nums[i] >= temp[-1]:
                    visited.add(nums[i])
                    temp.append(nums[i])
                    dfs(i+1, temp)
                    temp.pop()
        
        dfs(0, [])
        return res