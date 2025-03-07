class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda tup: (tup[0]))

        newIntervals = [intervals[0]]
        for index in range(1,len(intervals)):
            if intervals[index][0] >= newIntervals[-1][1]:
                newIntervals.append(intervals[index])
            else:
                if newIntervals[-1][1] > intervals[index][1]:
                    newIntervals[-1] = intervals[index]

        return len(intervals) - len(newIntervals)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda tup: (tup[0]))

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                if end < prevEnd:
                    prevEnd = end
        return res







        





        