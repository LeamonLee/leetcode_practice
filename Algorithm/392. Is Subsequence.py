'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
i.e., "ace" is a subsequence of "abcde" while "aec" is not

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ''' Solution1 '''
        if not s: return True
        if len(s) > len(t): return False
        if s == t : return True

        '''
        思路: 使用two pointers
        s:  a           x           c
            matchCount
        t:  a           h           b           g           d           c
            i
        '''
        matchCount = 0
        for i in range(len(t)):
            if s[matchCount] == t[i]:
                # print(f"match {s[matchCount]}")
                matchCount+=1
                if matchCount == len(s): return True
        # print(f"matchCount:{matchCount}")
        return False


        ''' Solution2 (DP)反而比較慢 '''
        # if not s: return True
        # if len(s) > len(t): return False
        # if s == t : return True

        # ROWS = len(t) + 1   # 要記得+1
        # COLS = len(s) + 1   # 要記得+1

        # # dp = [[FALSE]*COLS]*ROWS  # <---這樣寫反而會錯
        # dp = [[False for _ in range(COLS)] for _ in range(ROWS)]

        # for r in range(ROWS):
        #     dp[r][0] = True
        
        # # print(f"dp1 :{dp}")
        # for r in range(1, ROWS):
        #     for c in range(1, COLS):
        #         if dp[r-1][c] == True:
        #             # print(f"case1 r:{r}, c:{c}")
        #             dp[r][c] = True
        #         elif s[c-1] == t[r-1] and dp[r-1][c-1]:
        #             # print(f"case2 r:{r}, c:{c}")
        #             dp[r][c] = True
        
        # # print(f"dp2 :{dp}")
        # return dp[-1][-1]

