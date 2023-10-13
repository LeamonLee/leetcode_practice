'''
You are given an array of strings tokens that represents an arithmetic expression 
in a Reverse Polish Notation.
Evaluate the expression. 
Return an integer that represents the value of the expression.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        '''
        這一題順序很重要，由於是stack，所以要把第二次pop出來的(num2)擺在前面
        例如["13","5","/"]，是13/5，但是13會先被push進stack，再來才是5，所以5會先被pop出來，再來才是13

        計算完結果後記得要再append進stack中
        '''

        for token in tokens:
            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 + num1)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(token))
        return stack.pop()