# 1480 Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

## Thoughts and Approach

In place replacement to save memory


## Python Code

```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(1,n,1):
            nums[i]+=nums[i-1]
        return nums
```

## Time Complexity

O(N)

## Space Complexity

O(1) 
