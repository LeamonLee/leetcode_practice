class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        res=""

        for i in range(len(s)):
            if i != len(s)-1:
                # res = res + self.reverse(s[i]) + " "
                res = res + s[i][::-1] + " "
            else:
                # res+=self.reverse(s[i])
                res += s[i][::-1]
        
        return res
    
    def reverse(self, s):
        l = 0
        r = len(s) -1
        s=list(s)

        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        
        return "".join(s)
