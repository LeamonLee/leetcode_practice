'''
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.


Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        
        paperCount = 0
        citations.sort()    # 一定要先經過排序!!!
        
        for i in range(len(citations)-1, -1, -1):
            paperCount+=1   # 目前paper數量
            if citations[i] < paperCount:   # 如果citation的數量小於當前paper數量，就不符合題目要求(至少要大於等於)，就要減1然後退出
                paperCount-=1
                break
        
        return paperCount