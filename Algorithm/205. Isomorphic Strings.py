'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if not s or not t: return False
        charMap = {}    # 使用hashmap紀錄字符一一對應的關係

        for i,c in enumerate(s):
            # 如果之前已經有紀錄在hashmap的key裡面，就看value是否和t的字符是一樣的
            if c in charMap:
                if charMap[c] == t[i]:
                    continue
                else:
                    return False
            # 如果之前沒有記錄在hashmap的key裡面
            else:
                # 但如果t的字符出現在hashmap的value裡，代表s有其他字符紀錄過了
                if t[i] in charMap.values():
                    return False
                charMap[c] = t[i]
        
        return True

