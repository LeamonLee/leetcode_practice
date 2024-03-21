'''
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1: return True
        firstChr = word[0]
        secChr = word[1]

        ''' 
        All uppercase 
        Ex: USA
        '''
        if firstChr.isupper() and secChr.isupper():
            '''
            會進到這個case代表前面兩個字都是大寫，所以從第三個字(index=2)開始檢查就可以
            '''
            for i in range(2, len(word)):
                # 如果有任何一個小寫，就return False
                if word[i].islower():
                    return False
        else:
            ''' 
            All characters from the second word are lowercase 
            因為第一個字不管大寫小寫都可以
            Ex: Leetcode, leetcode
            '''
            for i in range(1, len(word)):
                # 如果有任何一個大寫，就return False
                if word[i].isupper():
                    return False
        
        return True