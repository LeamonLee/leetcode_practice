'''
Given an integer array nums of unique elements, 
return all possible subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

-
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res=[]
        # subset=[]

        # '''
        # nums=[1,2,3]
        # '''

        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return
            
        #     subset.append(nums[i])
        #     dfs(i+1)

        #     subset.pop()
        #     dfs(i+1)
        
        # dfs(0)
        # return res

        # ===============================================

        '''
        這題給定的nums沒有重複的element
        '''

        res=[]

        def backtrack(startIdx, temp):
            '''
            這題關鍵就是 backtracking沒有任何的停止條件。
            且空陣列也算結果之一。且[1,2]和[2,1]是一樣的
            '''
            res.append(temp.copy())

            for i in range(startIdx, len(nums)):
                temp.append(nums[i])
                backtrack(i+1, temp)        # startIdx還是要往上+1
                temp.pop()
        
        backtrack(0, [])
        return res