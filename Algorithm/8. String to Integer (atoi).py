'''
Example 1:
Input: s = "42"
Output: 42

Example 2:
Input: s = "   -42"
Output: -42

Example 3:
Input: s = "4193 with words"
Output: 4193
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        MAX_INT = (1 << 31) - 1
        MIN_INT = -1 * (1 << 31)

        # Remove whitespace
        while index < len(s) and s[index] == ' ':
            index+=1
        
        if index == len(s):
            return 0
        
        isPositive = True
        # check sign
        if s[index] == '+':
            index+=1
        elif s[index] == '-':
            index+=1
            isPositive = False
        
        currNum = 0
        while index < len(s):
            # 透過減去0的ASCII，判斷是0~9的哪一個
            digit = ord(s[index]) - ord('0')
            # print(f"index:{index}, s[index]:{s[index]}, digit:{digit}")
            
            # 如果超過0~9代表不是數字
            if digit < 0 or digit > 9:
                break
            
            # 判斷是否overflow，currNum在51行 乘以10之前，先看有沒有大於最大(小)值除以10
            if currNum > MAX_INT // 10 or \
                (currNum == MAX_INT // 10 and digit > MAX_INT % 10):
                # print("overflow")
                return MAX_INT if isPositive else MIN_INT

            currNum = currNum * 10 + digit
            index+=1
        
        return currNum if isPositive else -1*currNum

