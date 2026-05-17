# 1929 Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

## Thoughts and Approaches

Build an array of size 2 * n and assign nums[i] to ans[i] and ans[i + n]

## Python Code

```Python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(n*2)
        for i, x in enumerate(nums):
            ans[i]=x
            ans[i+n]=x
        return ans
```

## Time Complexity
O(n)

## Space Complexity
O(1) 
