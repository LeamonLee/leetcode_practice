'''
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        charIndexMap = {}   # 記錄每個character在s的index
        maxLen = 1
        l = 0

        '''
        s:  pwwkew
            l       <--- l是不重複字串的index起點
            r       <--- r會隨著for迴圈一直往前走，並記錄每個character的index
        '''
        for r in range(len(s)):
            c = s[r]
            if c in charIndexMap:               # 如果發現重複的character，就把l移動到重覆index的前面
                l = max(l, charIndexMap[c]+1)
            
            maxLen = max(maxLen, r-l+1)
            charIndexMap[c] = r
        
        return maxLen
