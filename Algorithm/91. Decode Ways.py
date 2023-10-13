'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters 
using the reverse of the mapping above (there may be multiple ways). 

For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0

        '''
        這一套是一個DP的題目，
        因為當前這一步有多少種組合，只和前一步或者前兩部有關係，
        例如可以把前一步和前兩步的數字當成一個整體，這時候當前步自己是一個整體，這時看dp前一步有多少種組合
        也可以把當前步和前一步當成一個整體，這時候看dp前兩步有多少種組合
        '''

        # dp = [0]*(len(s)+1)
        
        # dp[0]=1
        # dp[1]=1
        # for i in range(1, len(s)):
        #     if s[i] != '0':
        #         dp[i+1]+=dp[i]
            
        #     num = int(s[i-1:i+1])
        #     if num >= 10 and num <= 26:
        #         dp[i+1]+=dp[i-1]
        
        # return dp[-1]

        ####################################################

        dp = [0]*(len(s))
        
        dp[0]=1 # 第一個字符只有自己一步，所以初始化為1
        for i in range(1, len(s)):
            # 如果當前這一步自己不是0，代表前面一步有多少種可能，到當前這一步就還是維持有多少種組合
            if s[i] != '0':
                '''
                因為一開始dp[i]初始化為0，所以這邊用dp[i]+=dp[i-1]或是dp[i]=dp[i-1]都可以
                '''
                # dp[i]+=dp[i-1]
                dp[i]=dp[i-1]
            
            # 接著把前一步和當前自己這一步合在一起看，
            # 如果範圍在10~26之間，代表這也是一種組合，因此可以把前兩步有多少種組合也加進來
            num = int(s[i-1:i+1])
            if num >= 10 and num <= 26:
                if i>1:
                    dp[i]+=dp[i-2]
                else:
                    dp[1]+=dp[0]

            
        
        print(f"dp:{dp}")
        return dp[-1]