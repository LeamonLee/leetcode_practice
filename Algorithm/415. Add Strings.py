'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

可和67. Add Binary比較做法
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1)-1
        p2 = len(num2)-1

        res=[]
        carry=0
        while p1 >= 0 or p2 >= 0:   # 用or條件
            n1 = int(num1[p1]) if p1>=0 else 0
            n2 = int(num2[p2]) if p2>=0 else 0

            total = n1+n2+carry

            # 10進位的算法
            carry = total // 10
            remainer = total % 10
            res.insert(0, str(remainer))

            p1-=1
            p2-=1
        
        if carry:
            res.insert(0, str(carry))
        
        return "".join(res)

