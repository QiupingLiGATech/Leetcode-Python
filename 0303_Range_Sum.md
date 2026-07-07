# 303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

## Thoughts and Approaches

In general, any subarray can be viewed as a prefix with an earlier prefix removed. Therefore, the sum of any subarray can be expressed as the difference between two prefix sums.

As a result, if we preprocess the prefix sums of nums, we can compute the sum of any subarray in O(1) time.

Note: self.s[i + 1] = self.s[i] + x By using s[i] + x to calculate the next value, the code avoids re-summing the array from scratch every time. It builds the entire history in a single, efficient O(n) pass by always building on top of the last number it computed.

## Python Code

```Python
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.s = [0] * (len(nums) + 1) ## 1 s 的长度是 len(nums)+1 因为考虑了 the sum of zero elements. 因为left 可能会是0
   
        ### 计算 self.s[i+1] 在 s[i]的基础上+x; 降低了时间复杂度。 By using s[i] + x to calculate the next value, the code avoids ## ##re-summing the array from scratch every time. It ## builds ### the entire history in a single, efficient O(n) pass by ## always building on top of the last number it computed.
        for i, x in enumerate(nums):
            self.s[i + 1] = self.s[i] + x  #### 2 s[i]: the sum of the first i elements: from a[0] to a[i-1]
                                           #### s[i+1]: the sum of the first i+1 elemetns, including from a[0] to a[i]



    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left] ##3 第一项： a[0] 到a[right]; 第二项： a[0] 到 a[left-1] 


##1. Why do we need s[i + 1]?
##When we initialize the prefix sum array s, we make it one element longer than the original nums array, starting with a 0.

## s[0] is always 0 (it represents the sum of "zero elements").

## s[1] stores the sum of the first element (nums[0]).

## s[2] stores the sum of the first two elements (nums[0] + nums[1]).

## s[i + 1] stores the sum of everything up to nums[i].

```
## Time Complexity
O(n)

## Space Complexity
O(n) 

