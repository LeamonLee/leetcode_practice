'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 
Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        這題要反向思考，從後面算回來，最後再reverse
        '''
        res=""
        while columnNumber > 0:
            columnNumber-=1 # 記得要減1
            result = columnNumber % 26
            res+=chr(ord("A")+result)
            columnNumber=(columnNumber // 26)
        
        return res[::-1]