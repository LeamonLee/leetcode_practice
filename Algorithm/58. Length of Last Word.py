'''
Given a string s consisting of words and spaces, 
return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.


Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1    # 從字串最後的index開始往左邊遞減算

        # 先移除空格，遇到空格就繼續往左(i-=1)
        while i>=0 and s[i]==' ':
            i-=1
        
        count = 0
        # 如果不是空格了，就可以開始算字數
        while i>=0 and s[i]!=' ':
            count+=1
            i-=1
        
        return count