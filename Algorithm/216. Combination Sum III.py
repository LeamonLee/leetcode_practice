'''
Problem
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers. The solution set must not contain duplicate combinations. 

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]

        def backtrack(_target, temp, count, start_idx):
            if count < 0 or _target < 0: return
            if _target == 0 and count == 0:
                res.append(temp.copy())
                return
            
            for num in range(start_idx, 10):    # <-- 只能是1~9的數字
                temp.append(num)
                backtrack(_target-num, temp, count-1, num+1)    # <-- 最後一個參數是num+1不是start_idx+1
                temp.remove(num)
            
        backtrack(n, [], k, 1)
        return res