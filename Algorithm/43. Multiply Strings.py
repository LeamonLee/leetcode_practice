'''
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

-
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
        
        '''
        本題關鍵: 每個字符用ord去算和'0'的ASCII差異，就可以知道是0~9
        '''

        def convert2Int(s):
            currNum = 0
            for i in range(len(s)):
                currNum = currNum*10 + (ord(s[i]) - ord('0'))   #   用ASCII計算
            
            return currNum
        
        return str(convert2Int(num1) * convert2Int(num2))