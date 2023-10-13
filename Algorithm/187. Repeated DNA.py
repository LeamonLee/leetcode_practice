class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        slideWindowCount = len(s) - 10 + 1  # 假設s字串長度11，11-10+1=2，代表總共可以移動兩次
        '''
        使用兩個hashSet紀錄重複出現的字串(repeated string)
        '''
        seen = set()
        repeated = set()
        for l in range(slideWindowCount):
            subString = s[l:l+10]
            if subString in seen:
                repeated.add(subString)
            else:
                seen.add(subString)
        
        return repeated