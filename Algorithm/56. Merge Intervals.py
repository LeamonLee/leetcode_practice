'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        這題就是將原本有重疊的array變成沒有重疊
        '''
        res=[]

        '''
        因為題目沒有說會幫我們排序好
        排序完後可以確保每個item的第一個element都是照順序由小到大排列好的
        '''
        intervals = sorted(intervals, key=lambda item: item[0]) # 先用第1個element排序

        curr = intervals[0]
        for i in range(1, len(intervals)):  # 從1開始
            # 拿當前的第2個和下一個的第1個比較
            if curr[1] < intervals[i][0]:   # 如果比較小代表不用融合
                res.append(curr)
                curr = intervals[i]
            else:                           # 如果比較大，就和下一個的第2個比較誰比較大
                curr[1] = max(curr[1], intervals[i][1])
        
        # 還有剩餘最後一次的curr要加進來
        res.append(curr) # <--- 這一步很重要

        return res