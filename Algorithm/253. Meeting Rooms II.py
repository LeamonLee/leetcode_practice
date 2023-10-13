'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
'''

from typing import (
    List,
)
from lintcode import (
    Interval,
)
import heapq 
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here

        lstStart = sorted([i.start for i in intervals])
        lstEnd = sorted([i.end for i in intervals])

        sIdx, eIdx = 0, 0
        res, count = 0, 0

        while sIdx < len(intervals):
            startTm = lstStart[sIdx]
            endTm = lstEnd[eIdx]

            if startTm < endTm:
                sIdx+=1
                count+=1
            else:
                eIdx+=1
                count-=1
            res=max(res, count)
        
        return res

        ''' Didn't work '''
        # print(f"intervals:{intervals}")
        # intervals.sort(key=lambda item: item.start)
        # heapQueueEndTime=[]
        # heapq.heappush(heapQueueEndTime, (intervals[0].end, intervals[0]))

        # res=1
        # for i in range(1, len(intervals)):
        #     curr = intervals[i]
        #     prev = heapq.heappop(heapQueueEndTime)[1]
        #     print(f"heapQueueEndTime:{heapQueueEndTime}")
        #     print(f"prev.start:{prev.start}, prev.end:{prev.end}")
        #     if curr.start >= prev.end:
        #         prev.end=curr.end
        #     else:
        #         res+=1
        #         heapq.heappush(heapQueueEndTime, (curr.end, curr))
            
        #     heapq.heappush(heapQueueEndTime, (prev.end, prev))
        
        # return res
