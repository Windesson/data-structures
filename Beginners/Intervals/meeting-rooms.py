class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        
        intervals = sorted(intervals, key=lambda tup: (tup[1]) )

        for index in range(0, len(intervals) -1):
            curr_end = intervals[index][1]
            next_start = intervals[index+1][0]

            if curr_end > next_start:
                return False

        return True 
    
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True

        meetings = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if meetings:
                for meeting in meetings:
                    ok = (end <= meeting[0] or start >= meeting[1])
                    if not ok:
                        return False

            meetings.append(interval)

        return True 