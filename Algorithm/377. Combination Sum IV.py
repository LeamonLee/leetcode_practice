'''
Example:
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
'''

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # if not nums: return 0

        # dp = [0]*(target + 1)
        # dp[0] = 1
        
        # for t in range(1, len(dp)):
        #     for num in nums:
        #         if t - num >= 0:
        #             dp[i] += dp[t - num]  # 例如t=7, num=3, 如果dp[4]有2種組合([2,2] and [1,3])的方法，那如果要組成dp[7]，當然就可以直接加上2，因為[2,2,3]或是[1,3,3]
            
        # return dp[-1]

        #################################
        '''
        target:1
            [1]
        target:2
            [1,1]
            [2]
        target:3
            [1,1,1]
            [3]
            [1,2]
            [2,1]
        target:4
            (1, 1, 1, 1)    <--- target 3的加上1
            (3, 1)          <--- target 3的加上1
            (1, 2, 1)       <--- target 3的加上1
            (2, 1, 1)       <--- target 3的加上1
            (1, 1, 2)       <--- target 2的加上2
            (2, 2)          <--- target 2的加上2
            (1, 3)          <--- target 1的加上3
        '''
        if not nums: return 0
        dp = [[] for _ in range(target+1)]  # 假設target=5，則dp長度為6，因為還包含0

        for t in range(1, len(dp)): # 假設target=5，則dp長度為6，因此for迴圈從1跑到5
            for num in nums:
                if num-t > 0: continue              # 如果num比t大則跳過
                if num-t == 0: dp[t].append([num])  # 如果num=t，則append自己(num)進來，因為每個target本來就會包含自己(如果nums裡面有這個element的話)。

                for _res in dp[t-num]:
                    dp[t].append(_res+[num])
        
        print(f"dp:{dp}]")
        return len(dp[-1])

if __name__ == "__main__":
    s = Solution()
    result = s.combinationSum4(nums=[1, 2, 3], target=4)
    print(f"result:{result}")