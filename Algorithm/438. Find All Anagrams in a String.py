'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        
        '''
        思路: 用兩個hashmap各自紀錄s和p中每個字符出現的次數
        '''
        sCount={}
        pCount={}
        l=0

        '''
        用sliding window的方式
        s = "cbaebabacd"
             l  r
              l  r
               l  r
                l  r   
        p = "abc"
        len(p)=3，因此r從index 3開始
        '''
        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
        
        res = [0] if sCount == pCount else []

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -=1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l+=1
            if sCount == pCount:
                res.append(l)
        
        return res
