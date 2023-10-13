'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        先從第一個string全部的字開始比較，如果不匹配就一個一個遞減。
        '''
        pre = strs[0]

        for i in range(1, len(strs)):
            item = strs[i]
            while not item.startswith(pre):
                pre = pre[:len(pre)-1]
        
        return pre