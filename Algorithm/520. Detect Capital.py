class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1: return True
        firstChr = word[0]
        secChr = word[1]

        ''' All uppercase '''
        if firstChr.isupper() and secChr.isupper():
            for i in range(2, len(word)):
                if word[i].islower():
                    return False
        else:
            ''' All characters from the second word are lowercase '''
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
        
        return True