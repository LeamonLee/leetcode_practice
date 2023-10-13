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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        '''
        [1] -> [1,2], [2,1] -> [3,1,2], [1,3,2], [1,2,3]
        '''

        def dfs(perms, i):
            print(f"perms:{perms}, i:{i}")
            if len(perms) == len(nums):
                print(f"Found perms:{perms}")
                res.append(perms)
                return

            
            for j in range(i+1):
                print(f"j:{j}")
                tmp = perms.copy()
                tmp.insert(j, nums[i])
                dfs(tmp, i+1)         
 
        
        dfs([], 0)
        return res