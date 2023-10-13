class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr = 1
        pre = 0
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr+=1
            else:
                res += min(curr, pre)
                pre = curr
                curr = 1
        
        res += min(curr, pre)   # 最後還是需要再加一次
        return res