'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei), determine if a person could attend all meetings.

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
'''

from typing import (
    List,
)
from lintcode import (
    Interval,
)

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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        
        intervals.sort(key=lambda item: item.start)
        for i in range(1, len(intervals)):
            prevInt = intervals[i-1]
            currInt = intervals[i]

            if currInt.start < prevInt.end: return False
        
        return True
