'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}
        l = 0
        maxCount = 0        # 計算目前每個英文字母出現的次數 最多的有幾次
        maxSubString = 0    # response

        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r], 0)
            maxCount = max(maxCount, countMap[s[r]])

            '''
            k代表最多能置換的次數，r-l+1為window的寬度，
            假設k=2, maxCount=3, r-l+1=6, 6-3=3>2，
            代表在字串長度為6的字串中，目前字符重複最多次為3，
            其他3個字符需要靠置換才能有最大的repeating character，
            但k=2代表最多只能置換兩次，所以條件不成立
            '''
            while (r-l+1) - maxCount > k:
                countMap[s[l]] -= 1
                l+=1
            
            if (r-l+1) - maxCount <= k:
                maxSubString = max(maxSubString, r-l+1)
        
        return maxSubString


