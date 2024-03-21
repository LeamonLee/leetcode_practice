'''
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

可與242, 383比較
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        思路:使用hashmap來記錄每個字符出現的頻率
        '''
        dctCount = {}
        for char in s:
            dctCount[char] = dctCount.get(char, 0) + 1
        
        # 最後再跑一次for迴圈看哪一個字符只出現1次
        for i in range(len(s)):
            if dctCount[s[i]] == 1:
                return i
        
        return -1