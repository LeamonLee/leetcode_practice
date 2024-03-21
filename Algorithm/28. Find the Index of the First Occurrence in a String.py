'''
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

-
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lengthHaystack = len(haystack)
        lengthNeedle = len(needle)
        if not haystack or lengthHaystack < lengthNeedle: return -1 # 如果haystack本身就比needle長度還短，那連比都不用比
        if not needle: return 0 # 如果needle為空字串，就直接回傳0

        '''
        - 從haystack第一個字符開始跑for loop
        - i是haystack的起始字符
        '''
        for i in range(lengthHaystack):
            if haystack[i] == needle[0]:    # 先比較needle的第一個字元
                ptr = 1 # 目前符合needle字串的長度
                while i+ptr < lengthHaystack and \
                        ptr < lengthNeedle and \
                        haystack[i+ptr] == needle[ptr]:
                    ptr+=1
                
                if ptr == lengthNeedle: return i    # 因為i是haystack的起始字符
        
        return -1