'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"

        res=list(s)
        l=0
        r=len(s)-1
        while l<r:
            while l<r and s[l] not in vowels:
                l+=1
            while l<r and s[r] not in vowels:
                r-=1
            
            res[l], res[r] = res[r], res[l]
            l+=1
            r-=1
        
        return "".join(res)