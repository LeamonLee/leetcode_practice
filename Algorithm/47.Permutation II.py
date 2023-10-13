'''
Problem:
Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.

For example, [1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        這題關鍵在nums是有包含重複數字的array
        '''
        ''' Solution1 採用一個dictionary紀錄每個字符出現的次數，接著跑for loop遍歷整個dictionary'''
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
            1: 2,
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
    
        ''' Solution2 '''

        # res=[]
        
        # def backtrack(temp:list, visited:set):
        #     if len(temp) == len(nums):
        #         res.append(temp.copy())
        #         return
            
        #     for i in range(len(nums)):
        #         # 防止重复使用自己
        #         if i in visited: continue
                
        #         # 防止重复使用同样的数字，
        #         # 舉例: [1,1,2]，當i=1時，這時i=0已經從visited remove了，但其實for迴圈跑i=0時已經把[1,1,2]這個case加進res過了，所以當i=1時就不用再跑一次。
        #         # 還是要用(i-1)not in visited的原因，因為最一開始跑i=0的case時，res還沒有[1,1,2]，當跑到i=1時，這時visited是有i=0的，所以不能continue。
        #         if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited: continue

        #         temp.append(nums[i])
        #         visited.add(i)
        #         backtrack(temp, visited)
        #         temp.pop()
        #         visited.remove(i)
        
        # backtrack([], set())
        # return res




if __name__ == "__main__":
    s=Solution()
    result = s.permuteUnique(nums=[1,1,2])
    print(f"result:{result}")