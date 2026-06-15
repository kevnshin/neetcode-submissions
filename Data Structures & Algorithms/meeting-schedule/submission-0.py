"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            interval_1 = intervals[i - 1]
            interval_2 = intervals[i]
            if (interval_2.start < interval_1.end):
                return False
        return True 

    
        