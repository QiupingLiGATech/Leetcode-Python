# 1502. Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

## Thoughts and Approaches
One Pass

## Python Code
```Python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n=len(arr)
        if n==2: return True
        fixed=arr[1]-arr[0]
        for i in range(2,n,1):
            if arr[i]-arr[i-1]==fixed:
                continue
            else:
                return False
        return True
```

## Time Complexity

O(n log n)

## Space Complexity

o(n)
