'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res=[]
        self.backtrack("", n, n)
        return self.res

    '''
    傳入left和right兩個參數，分別代表左括號和右括號的數量
    '''
    def backtrack(self, curr, left, right):
        if left == 0 and right == 0:
            self.res.append(curr)
            return
        
        if left > 0:
            self.backtrack(curr+"(", left - 1, right)
        
        # 右括號只有當數量小於左括號時才跑backtracking
        # 因為一定要先有左括號，才會有右括號
        if right > left:
            self.backtrack(curr+")", left, right-1)
        
