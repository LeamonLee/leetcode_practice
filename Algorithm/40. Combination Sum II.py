'''
Problem:
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers. The solution set must not contain duplicate combinations. 

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        這一題和上一題不一樣，
        且candidate本身可能含有重複數字
        candidates裡面的數字不行重複使用
        '''

        ''' Backtracking '''
        res=[]
        candidates.sort()   # <--------這一步很重要!! 目的是為了去除重複

        def backtrack(_target, temp, start_idx):
            if _target < 0: return
            if _target == 0:
                res.append(temp.copy())
                return
            
            for i in range(start_idx, len(candidates)):
                # 第90題也有用到這招
                # 這一部很重要!是這題去掉重複的關鍵，因為candidates裡面的數字可能會重複，
                # 例如有兩個1，但是第一個1和第二個1都可以構成[1,7]來達成target的8，
                # 所以如果第一個1已經有[1,7]了，第二個1就不用再跑一次
                if i > start_idx and candidates[i] == candidates[i-1]: continue
                
                temp.append(candidates[i])
                backtrack(_target-candidates[i], temp, i+1) # candidates裡面的數字不行重複使用，所以必須i+1
                temp.remove(candidates[i])
        
        backtrack(target, [], 0)
        return res