# 253 Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

## Thoughts and Approaches

We can't really process the given meetings in any random order. The most basic way of processing the meetings is in increasing order of their start times and this is the order we will follow. 
Sorting part is easy, but for every meeting how do we find out efficiently if a room is available or not?
we can keep all the rooms in a min heap where the key for the min heap would be the ending time of meeting. 
So, every time we want to check if any room is free or not, simply check the topmost element of the min heap as that would be the room that would get free the earliest out of all the other rooms currently occupied.
If the room we extracted from the top of the min heap isn't free, then no other room is. So, we can save time here and simply allocate a new room.

Why len(ending_time) is the Answer?

its final size actually represents the maximum number of overlapping meetings (the peak demand) seen during the entire day. This heap only increase or stay the same, it never decreases.

## Python Code

```Python
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        endingTime=[]
        intervals.sort(key=lambda x:x[0])

        #add the first meeting
        heapq.heappush(endingTime, intervals[0][1]) ## push [[meeting ending time]] into min heap; 1 room that frees up at intervals[0][1]


       #for all the remaining meeting:
        for x in intervals[1:]:
            if endingTime[0]<=x[0]: #check whether you can free up that previous meeting
                heapq.heappop(endingTime) ###meeting with the earlest ending time came to an end; 

            heapq.heappush(endingTime, x[1]) ##add another meeting room, to accomodate another meeting        

        return len(endingTime)

```

## Time Complexity
O(NlogN)

## Space Complexity
O(N)
