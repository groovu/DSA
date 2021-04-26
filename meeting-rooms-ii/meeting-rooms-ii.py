class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    # start by sorting meetings by start times.
    # iterate through time and add rooms at needed.
    # you don't care how long a meeting last for
    # you just need to know when a meeting start and ends.
    # split start and ends into two lists and sort them both
    # now you have a chronological order you can use to compare to each other.
    # irl: a meeting start, you check if rooms are avail, if not add a room.
    # if a meeting starts before another meeting ends, meeting can go to avail room or make another room.
    
        startTimes = []
        endTimes = []
        for time in intervals:
            startTimes.append(time[0])
            endTimes.append(time[1])

        startTimes.sort() # sorting lets us compare chronological times
        endTimes.sort()   # if the next starting < the next ending, 

        startIndex = 0
        endIndex = 0

        numRooms = 0
        avail = 0

        while startIndex < len(startTimes): # loop through all start times
            if startTimes[startIndex] < endTimes[endIndex]: # if start time < earliest end time, meeting goes to avail room or a new room.
                if avail == 0:
                    numRooms += 1
                else:
                    avail -= 1

                startIndex += 1

            else: # start is before an ending, add a new room and increment endIndex 
                #so we can check the ending of the next meeting.
                # startIndex does not incremenent, it will be checked with the new ending of the next meeting.
                avail += 1
                endIndex += 1


        return numRooms