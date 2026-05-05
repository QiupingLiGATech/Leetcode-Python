# 452. Minimum Number of Arrows to Burst Balloons
[Leetcode Problem](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


## My Thoughts
Greedy: I want the overlapping balloon to be put together, so that I can use one arrow to burst all of them. overall, I will use the minimum nubmer of arrows. 
Therefore we want to sort the balloons. 
if a balloons starting point is bigger than the previous balloon's ending point, then these two balloons do not overlap. then we need one more arrow. 
otherwise, a baloon's starting point is smaller than or equal to the previous balloon's ending point, these two balloons overlaps. we do not need one more arrow. 

### Difficulty
when two balloons overlap, what about the third balloon which also overalaps with these two???

Now we will look at the smaller right end because we want to burst both baloons. Then compare this right end, with the new balloon's staring point. 

## Two ways to solve this problem

## 1. Sort the baloons by their starting points.
```python

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]: # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1     
            else:
                points[i][1] = min(points[i - 1][1], points[i][1]) # 难点在这里: 更新重叠气球最小右边界; 方便确认一箭双雕or3雕？
        return result
```

## 2. Sort the baloons by their ending points
```python
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x : x[1]) ## sort by x end        
        arrows = 1
        pop = points[0][1]
        for x_start, x_end in points:
            if x_start>pop:   # if the current balloon starts after the end of another one, one needs one more arrow
                arrows += 1
                pop = x_end
            else:
                continue  
        return arrows
```

## 3. Comparision Table

Sort by End	Place arrow at the end： If the next balloon starts after the arrow, shoot a new one.	（Simpler) 
Sort by Start	Must track the "minimum end seen so far" to ensure you don't overshoot a short balloon.	(More Complex) 




