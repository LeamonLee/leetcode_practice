'''
You are given an array of non-overlapping intervals intervals 
where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
and intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending 
order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        isAdded = False # 紀錄newInterval是否已經被insertS

        '''
        這題題目有說已經先幫你根據每個element的start排序好了
        '''

        for i in range(len(intervals)):
            # 這是一個技巧，取各自第一個item的最大值，和各自第二個item的最小值
            # 如果第一個item<=第二個item代表有重疊
            # Ex: (1,3),(2,5)=>start=2,end=3, start<=end.   有重疊 
            # (1,3),(4,6)=>start=4,end=3, start>end.        沒有重疊
            start = max(newInterval[0], intervals[i][0])
            end = min(newInterval[1], intervals[i][1])

            if start <= end:    # 代表有重疊
                # 講兩個interval merge起來，並更新newInterval
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:   # 沒重疊
                # 確認newInterval的end是否比當前interval的start還小，如果比較大就和下一個interval比
                if newInterval[1] < intervals[i][0] and not isAdded:
                    res.append(newInterval)
                    isAdded = True
                
                # 記得要同時append intervals[i]到res
                res.append(intervals[i])
        
        if not isAdded:
            res.append(newInterval)
        
        return res