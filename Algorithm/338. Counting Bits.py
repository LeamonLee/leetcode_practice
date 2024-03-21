'''
Problem
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num, calculate the number of 1’s in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]
'''

'''
        只保留末尾1的方法:
        n = (n & -n)
          = 110 & 010
          = 010 


        消去n末尾的1的兩種方法，
        方法1:
        n=110:
        n = n & (n - 1) = 110 & 101 = 100
        
        或者 n = 111
        n = n & (n-1) = 111 & 110 = 110

        方法2:
        n = n - (n & -n) 
        n&-n = 110 & (010) = 010
        n - (n & -n) = 110 - 010 = 100
        
        或者 n = 111
        n&-n = 111 & 001 = 001
        n - (n&-n) = 111 - 001 = 110

'''

from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)

        for i in range(1, n+1):
            # 例如6=110, 先去除最後一個1後是100，這時可以去看100有幾個1過了，就不用重頭開始算
            dp[i] = dp[i & (i-1)] + 1       # 方法1
            # dp[i] = dp[i - (i & -i)] + 1  # 方法2

        return dp
        
if __name__ == "__main__":
    s = Solution()
    result = s.countBits(10)
    print(f"result:{result}")