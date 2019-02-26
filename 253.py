# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        time =0
        def func(intervals):
            endtime =0
            intervals.sort(key=lambda x:x.start)
            pointer =0
            while pointer<len(intervals):
                if intervals[pointer].start>=endtime:
                    endtime = intervals[pointer].end
                    del intervals[pointer]
                else:
                    pointer+=1
            print [ (s.start,s.end) for s in intervals ]
        while intervals:
            func(intervals)
            time+=1
        return time