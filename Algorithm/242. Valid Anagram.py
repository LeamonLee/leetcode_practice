'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

可與383, 387比較
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        if len(s) != len(t): return False

        '''
        使用hashmap紀錄每個character的出現次數
        s的+1，t的-1，
        最後再遍歷一次hashmap，如果發現不等於0，就不是anagram
        '''
        hashMap = {}
        for i in range(len(s)):
            hashMap[s[i]] = hashMap.get(s[i], 0) + 1
            hashMap[t[i]] = hashMap.get(t[i], 0) - 1
        
        for v in hashMap.values():
            if v != 0: return False
        
        return True
        