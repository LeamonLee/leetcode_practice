'''
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. 
If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.
Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:
Input: a = "a", b = "aa"
Output: 2
'''

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        curr=""
        res=0
        while len(curr) < len(b):
            curr+=a
            res+=1
        
        # 如果a="ab", b="ba"，這時需要再加一次a, a才會等於abab且包含ba
        if b not in curr:
            curr+=a
            res+=1
        
        if b in curr: return res
        else: return -1
