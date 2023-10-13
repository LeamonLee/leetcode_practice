'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        使用stack解這題
        '''
        stack=[]

        for c in s:
            if c == "(":
                stack.append(')')
            elif c == "{":
                stack.append('}')
            elif c == "[":
                stack.append(']')
            else:
                if not stack:
                    return False
                elif c != stack.pop():
                    return False
        
        # 如果for迴圈跑完還有stack，代表有殘留的左括號沒有被匹配到
        if stack: 
            return False
        else:
            return True 
