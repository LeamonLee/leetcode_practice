'''
Given a string s, return the longest palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''
class Solution:
    def __init__(self):
        self.left=0
        self.right=0
        self.maxLen = 0

    '''
    用雙指針判斷
    '''
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        for i in range(len(s)):
            self.helper(i, i)       # 為了aba這種case，一開始l和r都在中間b的位置
            self.helper(i, i+1)     # 為了abba這種case，一開始l和r在兩個b的位置
        return s[self.left:self.right+1]

    def helper(self, l, r):
        while l >= 0 and r < len(self.s) and self.s[l] == self.s[r]:
            if r-l+1 > self.maxLen:
                self.maxLen = r-l+1
                self.left=l
                self.right=r
            
            l-=1
            r+=1
