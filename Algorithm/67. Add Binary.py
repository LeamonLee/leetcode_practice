'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        直接將兩個字串中的每個字符用built-in的int轉換成integer
        接著將兩個數相加，記得加上carry(進位)，一開始carry=0
        加好之後因為是binary，只有0和1，因為要除以2和%2取商和餘數
        例如total加完等於3，則carry=3//2=1, remainer=3%2=1
        '''
        p1 = len(a)-1
        p2 = len(b)-1

        res=[]
        carry=0
        while p1 >= 0 or p2 >= 0:   # 用or條件
            num1 = int(a[p1]) if p1>=0 else 0
            num2 = int(b[p2]) if p2>=0 else 0

            total = num1+num2+carry
            ''' binary加法判斷carry and remainer的技巧 '''
            carry = total // 2
            remainer = total % 2
            res.insert(0, str(remainer))    # 一直從左邊append進array

            p1-=1
            p2-=1
        
        # 如果最後還有carry的話，要再insert進res
        if carry > 0:
            res.insert(0, str(carry))
        
        return "".join(res)