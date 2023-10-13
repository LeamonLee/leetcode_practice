'''
Given an integer array nums that may contain duplicates, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

和78題做比較
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        這一題給定的nums有重複的element，但題目沒有說已經排序好，
        所以第一步要先排序，因為需要前後element比較來排除重複
        subset [1,2]和[2,1]是一樣的
        '''
        res=[]

        nums.sort() # 這一步非常重要，因為需要前後element比較來排除重複
        def backtrack(startIdx, temp):
            '''
            這題關鍵就是 backtracking沒有任何的停止條件
            '''
            res.append(temp.copy())

            for i in range(startIdx, len(nums)):
                '''
                第40題也有用到這招
                以Example1為例，
                這條件非常重要，當startIdx是0，
                此時如果i跑到2，也就是nums[i]等於第二個2的時候，temp=[1,2]
                前面已經出現1,2，所以加上第三個2變成1,2,2，是合理的。

                但是當startIdx=1時，變成由第一個2開始，temp=[1,2]，這時已經被加進res
                當i跑到2時，也就是nums[i]等於第二個2的時候，此時第一個2已經從temp pop出來
                這時如果temp繼續把第二個2加進去，temp=[1,2]，但res已經被加入過了，所以要skip。
                '''
                if i > startIdx and nums[i] == nums[i-1]: continue     # (O)
                # if i != startIdx and nums[i] == nums[i-1]: continue     # (O)
                # if i > 0 and nums[i] == nums[i-1]: continue           # (X)

                temp.append(nums[i])
                backtrack(i+1, temp)
                temp.pop()
        
        backtrack(0, [])

        return res