# 435. Non-overlapping Intervals
[Leetcode Problem](https://leetcode.com/problems/non-overlapping-intervals/description/)

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

## Thoughts: The "Earliest Deadline First" Intuition

The problem asks for the minimum number of removals, which is mathematically equivalent to finding the maximum number of non-overlapping intervals.

Right-End Sorting (The "Greedy" Winner): By picking the interval that ends as early as possible, you leave the maximum amount of remaining time for all other intervals. It is the most "selfish" choice in terms of time, but the most "generous" choice for the remaining schedule.

Left-End Sorting: Picking the interval that starts first tells you nothing about when it finishes. A meeting could start at 8:00 AM but last until 5:00 PM, blocking the entire day.

The Failure of Start-Time SortingIf you sort by the starting point, a "bad" interval (one that is very long) can appear first and force you into making a sub-optimal decision.

Example Case: [[1, 10], [2, 3], [3, 4]] By Start Point: You see [1, 10] first. If you take it, you must remove both [2, 3] and [3, 4]. (Total removed: 2)
By End Point: You sort them as [[2, 3], [3, 4], [1, 10]].Pick [2, 3]. It ends at 3.Next is [3, 4]. It starts at 3, which is $\geq$ the previous end. Keep it!
Next is [1, 10]. It starts at 1, which is $<$ 4. Remove it. (Total removed: 1)

## Code

```Python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ## Change Perspective: Find the most number of non-overlapping intervals.
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        prev_end=float('-inf') ## -inf converted to float number, to handle the first ending case.   
        NonOverLap=0
        for curr_start, curr_end in intervals:           
            if curr_start>=prev_end: ## this means no olverapping. 
                NonOverLap+=1
                prev_end=curr_end ## update prev_end and NonOverLap
            else: ### there is overlapping
                continue                
        return len(intervals)-NonOverLap
```
### The other approach is your sort by the staring point

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:x[0])
        prev_end=intervals[0][1]
        removed=0
        for x_start, x_end in intervals[1::]:
            if x_start<prev_end: ## there is overlap, I need to remove, which one to remove?
                removed+=1
                prev_end=min(prev_end, x_end) ## update prev_end
            else: ## There is no overlap. 
                prev_end=x_end ## update prev_end
        return removed
```

## Time Cmoplexity
O(nlogn) because of sorting

## Space Complexity
O(1)
