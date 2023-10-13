'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring


Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

-
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        mx=0
        stack=[-1]  # 先放上-1，因為如果s為"()))"，其實在第二個字元")"就已經有完整的valid parentheses了，此時長度為1-(-1)=2
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:   # 如果是右括號，且stack空了(代表前面沒有左括號了)，就把最新的index更新進去
                    stack.append(i)
                else:           # 代表之前有左括號
                    mx=max(mx, i - stack[-1])
        return mx