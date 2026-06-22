# 941 Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

## Thoughts and Approaches

One PASS is the most optimal strategy. 

Let's walk up from left to right until we can't: that has to be the peak. We should ensure the peak is not the first or last element. 
Then, we walk down. If we reach the end, the array is valid, otherwise its not.

## Python Code

```Python
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up: The Main Goal is the find peak Index
        while i <= N-2 and A[i+1]>A[i]:
            i += 1
            
        
        # At this step, i is the peak Index. peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i <= N-2 and A[i+1]<A[i]:
            i += 1

        return i == N-1 ## when i is able to reach the final element!!! 

```

## Time Complexity
O(n)

## Space Complexity
O(1) 
