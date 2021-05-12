class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if intervals == []:
            return True
        if len(intervals) == 1:
            return intervals[0][0] <= intervals[0][1]
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])

        start.sort()
        end.sort()

        check1 = start.pop()
        check2 = end.pop()

        using = "end"
        while check2 >= check1:
            check2 = check1
            if using == "end":
                check1 = end.pop()
                using = "start"
            else:
                check1 = start.pop()
                using = "end"

            if len(start) == 0 and len(end) == 0:
                return True

        return False