'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

可與242, 387比較
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        初始化一個26長度的array，因為英文字母a~z
        接著magazine出現過的字符就+1，ransomNote出現過的字符就減1
        最後再遍歷一次array，如果有發現count<0的情況，代表magazine沒有ransomeNote需要的字符
        '''
        lstChaCount = [0 for _ in range(26)]

        for c in magazine:
            lstChaCount[ord(c)-ord('a')]+=1
        
        for c in ransomNote:
            lstChaCount[ord(c)-ord('a')]-=1
        
        for count in lstChaCount:
            if count < 0: return False
        
        return True
