### 45. Jump Game II
###Problem Description 
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.


#### 1. My Thoughts and Solution Approach 
The Essence of the Greedy Strategy: In this problem, we don't care about the specific path taken to reach a point. Instead, we focus on the "Range of Coverage."
Think of it as scouting ahead while walking on a bridge. As you walk on your current bridge, you look for the best possible spot to build the next bridge to extend your reach as far as possible.


#### 2. Python Code Implemenation

```python
from typing import List 

class Solution:
    def jump(self, nums: List[int]) -> int:
        # If there's only one element, you are already at the destination.
        if len(nums) == 1:
            return 0
            
        count = 0              # Think of each jump as a bridge to be built; This is like Number of bridges built (jumps taken); 
        cur_bridge_max = 0     # The right endpoint of the currently built bridge
        next_bridge_max = 0    # The maximum reach of the potential next bridge
        
        # Traverse the array to find the optimal jumping points
        for i in range(len(nums)): 
            next_bridge_max = max(next_bridge_max, i + nums[i]) ## Step 1: Scouting Phase: At every point, update the plan: if we were to jump from here, what is furthest we could reach. 
            
            if i == cur_bridge_max:           ### Step 2: We hit the boundary of your current bridge. We need to build a new bridge, using our best plan. 
                count += 1                  
                cur_bridge_max = next_bridge_max  

                if cur_bridge_max >= len(nums) - 1: ### Step 3: Termination Check: if the current brige can reach the final point, we stop. 
                    break               
                
        return count
```
#### 3. Complexity Analysis

Time Complexity: O(n) We perform a single linear scan of the nums array 
Space Complexity: O(1) 
