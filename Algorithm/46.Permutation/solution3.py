'''
Problem: Given a collection of distinct numbers, return all possible permutations.

For example, [1,2,3] have the following permutations:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        perms = []
        dctNums={}
        for num in nums:
            if num not in dctNums:
                dctNums[num] = 1
            else:
                dctNums[num] += 1
        
        '''
        dctNums = {
            1: 1,
            2: 1,
            3: 1
        }
        '''

        def dfs():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return

            for num in dctNums:
                if dctNums[num] > 0:
                    perms.append(num)
                    dctNums[num] -= 1
                    dfs()
                    dctNums[num] += 1
                    perms.pop()
        
        dfs()
        return res