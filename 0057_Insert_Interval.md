# 57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

## Thoughts and Apporaches
3 Phases:  

Phase 1: All intervals that come strictly before the new interval; 

Critical Thinking After Phase 1: Case 1: Current start is smaller than new interval start (Overlap); Case 2: Current start is between the new interval's start and end (Overlap)
Case 3: Current start is strictly greater than the new interval's end (No Overlap / Phase 3)

Phase 2: Overlapping Cases: Merge all overlapping intervals with the new interval (包括前面说到的两种覆盖情况）

Phase 3: Add all remaining intervals that comes strictly after. 

## Python Code

```Python
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Add all intervals that come strictly before the new interval
        while i <= n-1 and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1 

        ## Critical Think: when you reach here, intervals[i][1] >= newInterval[0]; this includes 3 cases when compare
        ## intervals[i][0] 比整个new interval都小 （有overalap)；比整个new interval 都大（Phase 3 考虑的，无覆盖）
        ## 比开端点大但是比关端点小 （有overlap) 
        
        # Phase 2: Merge all overlapping intervals with the new interval (包括前面说到的两种覆盖情况）
        while i <= n-1 and intervals[i][0] <= newInterval[1]: 
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # Append the final merged single interval
        result.append(newInterval)
        
        # Phase 3: Add all remaining intervals that come strictly after
        while i <= n-1:            
            result.append(intervals[i])
            i += 1
            
        return result
```

## Time Complexity
O(n)

## Space Complexity
O(n) 




