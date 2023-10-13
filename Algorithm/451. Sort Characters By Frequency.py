'''
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        # 使用一個hashmap紀錄每個character出現的次數
        hashMap={}
        maxFreq=1

        for c in s:
            hashMap[c] = hashMap.get(c, 0) + 1
            maxFreq = max(maxFreq, hashMap[c])
        
        # 初始化bucket size，例如maxFreq=5的話，就初始化一個size=5的array
        lstBucket = []
        for _ in range(maxFreq+1):
            lstBucket.append([])

        # 接著遍歷hashmap，把每個頻率的字符放進對應的bucket
        # Ex: lstBucket = [[], ['a','c'], ['e'], ['d','k']
        for c, freq in hashMap.items():
            lstBucket[freq].append(c)
        
        # 從後往前遍歷，因為要先放頻率出現最多次的
        res=""
        for freq in range(len(lstBucket)-1, -1, -1):
            for c in lstBucket[freq]:
                for _ in range(freq):
                    res+=c

        ''' 不能用hashMap，因為要用array從最後一個element(最高頻率)往前遍歷 '''
        # dctBucket = {}
        # for c, freq in hashMap.items():
        #     if freq not in dctBucket:
        #         dctBucket[freq] = [c]
        #     else:
        #         dctBucket[freq].append(c)
        
        # res=""
        # for freq, bucket in dctBucket.items():
        #     for c in bucket:
        #         for _ in range(freq):
        #             res+=c
        return res
