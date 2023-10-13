'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern and not s: return True
        if not pattern or not s: return False
        
        sArr = s.strip().split()
        if len(pattern) != len(sArr): return False

        hashMap={}
        for i in range(len(pattern)):
            if pattern[i] in hashMap:
                if hashMap[pattern[i]] != sArr[i]: return False
            else:
                if sArr[i] in hashMap.values(): return False
                hashMap[pattern[i]] = sArr[i]
        
        return True