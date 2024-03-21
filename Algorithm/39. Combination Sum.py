'''
All numbers (including target) will be positive integers. 
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
    [
        [7],
        [2,2,3]
    ]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
    [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]
Constraints:
    All elements of candidates are distinct.

與40,46,47,78,90相比
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        candidate本身沒有重複數字
        但candidates裡面的數字可以重複使用，來達到target
        '''

        ''' Backtracking '''
        res=[]

        def backtrack(_target, temp, start_idx):
            if _target < 0: return
            if _target == 0:
                res.append(temp.copy())
                return
            
            for i in range(start_idx, len(candidates)):
                temp.append(candidates[i])
                backtrack(_target-candidates[i], temp, i)   # 因為candidates裡面的數字可以重複使用，所以i不用+1
                temp.remove(candidates[i])
        
        backtrack(target, [], 0)
        return res



        ''' DP Solution '''
        # dp = [[] for _ in range(target+1)]

        # for c in candidates:  # 這一題candidates一定要在for loop外層，因為num不能重複，例如[2,2,3], [2,3,2], [3,2,2]都算同一種
        #     for t in range(1, len(dp)):
        #         if c-t > 0: continue
        #         if c-t == 0: dp[t].append([c])

        #         for _res in dp[t-c]:
        #             dp[t].append(_res+[c])
        
        # return dp[-1]