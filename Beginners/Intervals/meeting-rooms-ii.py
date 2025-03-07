class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        startL = sorted([s[0] for s in intervals])
        EndL = sorted([e[1] for e in intervals])

        i,j = 0, 0
        count = res = 0
        while i < len(startL):
            if startL[i] >= EndL[j]:
                #meeting has end
                count -= 1
                j += 1
            else:
                #meeting has started
                count += 1
                i += 1
            res = max(res, count)

        return res
            


        