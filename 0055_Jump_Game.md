# 55. Jump Game

### Problem Description
You are given an array of non-negative integers `nums`, and you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.

### My Thoughts and Solution Approach
The core idea behind this problem is the **Greedy Algorithm**.

1.  **Key Variable**: We need to maintain a variable `max_reach`, which represents the furthest boundary we can currently reach.
2.  **Global Perspective**: Instead of getting stuck on a specific sequence of jumps, we allow `i` to iterate through every index, treating every position as a potential "starting point."
3.  **Dynamic Updates**:
    * If the current index `i` has not exceeded `max_reach`, it means this position is reachable.
    * At every reachable position, we update: `max_reach = max(max_reach, i + nums[i])`.
    * Once `max_reach` covers or exceeds the last index, we return `True`.
    * If at any point the index `i` exceeds `max_reach`, it means we are stuck (likely due to a 0 that we cannot jump over), so we return `False`.



### Code Implementation (Python)

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0 # Identifying max_reach is the key to solving this problem
        n = len(nums)
        
        # Iterate through every index and try using it as a starting point
        for i in range(n):
            # If the current index i exceeds the furthest reachable distance, 
            # it means there is a "gap" we cannot cross.
            if i > max_reach:
                return False
            
            # Update the furthest reachable position
            max_reach = max(max_reach, i + nums[i])
            
            # If the furthest reach covers the last index, return True early
            if max_reach >= n - 1:
                return True
                
        return False
```

### Complexity Analysis
Time Complexity: O(n)，We go over the nums only once.        
Space Complexity: O(1) 
