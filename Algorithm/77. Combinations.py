'''
Given two integers n and k, 
return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        這題要注意[1,2]和[2,1]是一樣的，所以只要算一次就好了
        '''
        nums=[i for i in range(1, n+1)] # 因為沒有0的選項，所以要從1開始
        res=[]

        ''' backtrack '''
        def backtrack(temp, start_idx, count):
            if count==0:
                res.append(temp.copy())
                return
            
            for i in range(start_idx, n):
                temp.append(nums[i])
                backtrack(temp, i+1, count-1)
                temp.remove(nums[i])
        
        backtrack([], 0, k)
        return res
