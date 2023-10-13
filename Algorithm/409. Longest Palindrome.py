'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        countTable = defaultdict(int)
        for c in s:
            countTable[c]+=1
        
        res=0
        for count in countTable.values():
            res+=(count//2) * 2

            # res%2==0 是為了只要進來一次，例如如果原本res=4，代表還沒有中間位，這時進來後加了1，變成5
            # 之後res不管怎麼加都會是奇數，因為上面的寫法always是偶數
            # count%2==1 是假如count如果奇數，可以擺放在中間位，例如: aacaa的c
            if res%2==0 and count%2==1:
                res+=1
        
        return res