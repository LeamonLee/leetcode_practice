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

與39,40,47相比
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        '''
        這題關鍵在nums都是沒有重複數字的array
        且要列出所有的組合，所以不能像combination sum一樣傳入start_idx且還i+1。
        '''

        def backtrack(perms):
            ''' 停止條件 '''
            if len(perms) == len(nums):
                res.append(perms.copy())
                return

            for num in nums:
                if num not in perms:
                    perms.append(num)
                    # print(f"perms append:{perms}, num:{num}")
                    backtrack(perms)
                    perms.pop()
                    # print(f"perms pop:{perms}, num:{num}")
                
        
        backtrack([])
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.permute(nums=[1,2,3])
    print(f"result:{result}")