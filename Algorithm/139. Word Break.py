'''
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict) # 先轉成hashset，之後判斷字串是否在此hashset裡面時比較快
        dp = [False] * (len(s)+1)   # 長度記得+1，dp的每個element代表s的字符位置前是否在wordDict裡面。
        dp[0] = True
        
        '''
        用l r雙指針
        r會從s=1到整個s的長度開始跑，
        l會從s=0到當前r的長度開始跑
        s=catsandog
          r
          l

           r
          l

            r
          l->

             r
          l-->

              r
          l--->    
        '''
        for r in range(1, len(s)+1):
            for l in range(r):
                if dp[l] and s[l:r] in wordDictSet:
                    dp[r]=True
                    break   # 這行很重要
        
        return dp[-1]

