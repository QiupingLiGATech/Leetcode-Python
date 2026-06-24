# 252. Meeting Rooms

You are given an array of meeting times intervals where intervals[i] = [starti, endi].

A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time t and starting at time t do not overlap.

​​​​​​​Return true if a person can attend all meetings. Otherwise, return false.

## Thoughts and Approaches

Sort First and Then check whether the nearest interval overlaps or not. 


## Python Code

```Python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ## check are any of the two intervals overlap with each other??
        intervals.sort()
        n=len(intervals)

        for i in range(1,n,1):
            if intervals[i][0]>=intervals[i-1][1]: ## this indicates NO Overlap
                continue
            else:
                return False
        return True
```

## Time Complexity
O(N Log N) 

## Space Complexity
O(N)
