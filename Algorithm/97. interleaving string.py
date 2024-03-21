'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings respectively, such that:
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        解題思路用dp
        '''
        len1=len(s1)
        len2=len(s2)
        len3=len(s3)

        # Corner Case
        if len1+len2 != len3: return False
        if len1 == 0 and len2 == 0 and len3 == 0: return True

        # 記得要用len1+1和len2+1
        # 因為這種字串的2D DP都會有一個(0,0)位置
        dp = [[False for _ in range(len2+1)] for _ in range(len1+1)]

        dp[0][0] = True
        # Iterate through the first row (s2)
        for c in range(1, len2+1):  # 記得要用len2+1，且從1開始
            # 如果前一個為True，且s2和s3的字符相同，則當前dp為True
            if dp[0][c-1] and s2[c-1] == s3[c-1]:
                dp[0][c] = True

        # Iterate through the first column (s1)
        for r in range(1, len1+1):  # 記得要用len1+1，且從1開始
            # 如果前一個為True，且s1和s3的字符相同，則當前dp為True
            if dp[r-1][0] and s1[r-1] == s3[r-1]:
                dp[r][0] = True

        # Iterate through the rest of elements (From left to right, then go to next row)
        for r in range(1, len1+1):  # 記得要用len1+1，且從1開始
            for c in range(1, len2+1):  # 記得要用len2+1，且從1開始
                # 如果前一個column為True，且
                if dp[r][c-1] and s2[c-1] == s3[r+c-1]:
                    dp[r][c] = True
                
                # 如果前一個row為True，且
                if dp[r-1][c] and s1[r-1] == s3[r+c-1]:
                    dp[r][c] = True
        
        # print(f"dp:{dp}")
        return dp[-1][-1]