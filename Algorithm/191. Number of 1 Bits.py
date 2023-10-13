'''
Problem
Write a function that takes an unsigned integer and returns the number of ‘1’ bits it has (also known as the Hamming weight).

Example 1:
Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011

Example 2:
Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0

        while n != 0:
            n &= (n-1)
            res+=1
        
        return res

        #################################

        # res = 0
        # for _ in range(32):
        #     lsb = n & 1
        #     if lsb == 1: res+=1
        #     n = n >> 1

        # return res


if __name__ == "__main__":
    s=Solution()

    result = s.hammingWeight(n=11)
    print(f"result:{result}")