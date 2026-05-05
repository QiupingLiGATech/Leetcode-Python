# 453. Minimum Moves to Equal Array Elements 
[Leetcode Problem] (https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/)

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0

## My Thoughts and Approaches

Incrementing n-1 elements by 1 is equivalent to decrementing 1 element by 1. So instead of thinking "raise everything else," think "lower one element each move."
To make all elements equal optimally, you want to bring everything down to the minimum value. 

## Why This Is Hard to Reason About Directly? 
If you try to simulate this, you face questions like:

Which element do I skip each move?
Should I always skip the largest? The smallest?
What's the target value — and it keeps moving up

The target isn't fixed. Every move raises the floor, so you'd be chasing a moving target. It's hard to derive a clean formula this way. Focusing on incrementing n-1 elements is correct 
but hard to compute directly because the target value drifts upward with every move. However, in the decrement 1 view, the target is fixed. it is always the current minimum value. 

## Python Code
```Python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
```
## Time Complexity
O(n) where n is the number of elements in the array. 

## Space Complexity
O(1)
