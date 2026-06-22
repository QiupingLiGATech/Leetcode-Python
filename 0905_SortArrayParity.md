# 905 Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

## Thoughts and Approaches

You need two pointers: one starting at the front (for evens) and one starting at the back (for odds). Start one pointer at the beginning and one at the end

## Python Code
```Python
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        
        while left < right: ## # 循环直到不足两个数; Used If, ElseIf, Else
            # If left is even, move right
            if nums[left] % 2 == 0:
                left += 1
            # If right is odd, move left
            elif nums[right] % 2 != 0:
                right -= 1
            # If left is odd and right is even, swap them
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return nums
```

## Time Complexity
O(n)，其中 n 是 nums 的长度。

## Space Complexity
O(1) 

