'''
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"
'''

class Solution:
    def toHex(self, num: int) -> str:
        hexMap=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e', 'f']

        if num==0: return '0'
        
        # 關鍵是負號的處理
        if num <0:
            num = num+2**32

        res=""
        while num!=0:
            # 每4位計算一次hex
            res = hexMap[num & 0b1111] + res
            num=num >> 4
        
        return res