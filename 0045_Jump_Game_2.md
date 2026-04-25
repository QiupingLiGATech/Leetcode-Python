### 45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.


#### 1. Problem Core & Greedy Concept
The Essence of the Greedy Strategy:
In this problem, we don't care about the specific path taken to reach a point. Instead, we focus on the "Range of Coverage."
Think of it as scouting ahead while walking on a bridge. As you walk on your current bridge, you look for the best possible spot
to build the next bridge to extend your reach as far as possible.


#### 2. Python Code Implemenation
```
from typing import List 

class Solution:
    def jump(self, nums: List[int]) -> int:
        # If there's only one element, you are already at the destination.
        if len(nums) == 1:
            return 0
            
        count = 0              # Number of bridges built (jumps taken)
        cur_bridge_max = 0     # The right endpoint of the currently built bridge
        next_bridge_max = 0    # The maximum reach of the potential next bridge
        
        # Traverse the array to find the optimal jumping points
        for i in range(len(nums)): 
            
            # STEP 1: Scouting Phase
            # At every point, update the "Backup Plan": if we were to jump from here, 
            # what is the absolute furthest we could reach?
            next_bridge_max = max(next_bridge_max, i + nums[i]) 
            
            # STEP 2: Commitment Phase (Reached the end of the current bridge)
            # When you hit the boundary of your current jump, you MUST jump again.
            if i == cur_bridge_max:  
                count += 1                  # Build the next bridge
                cur_bridge_max = next_bridge_max  # Extend your current territory to the best scouted point

                # STEP 3: Termination Check
                # If the current coverage already reaches or exceeds the last index,
                # we don't need to scout any further.
                if cur_bridge_max >= len(nums) - 1:
                    break               
                
        return count
```
#### 3. Complexity Analysis

Time Complexity: O(n) We perform a single linear scan of the nums array 
Space Complexity: O(1) 
