# 2966. Divide Array into Arrays with Max Difference

ou are given an integer array nums of size n where n is a multiple of 3 and a positive integer k.

Divide the array nums into n / 3 arrays of size 3 satisfying the following condition:

The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

## Thoughts and Approaches

Find array of size 3 based on index i: 

temp=nums[3*i:3*i+3]

## Python Code

```Python
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(int(n/3)):
            temp=nums[3*i:3*i+3] ## this is array of size 3
            if temp[2]-temp[0]>k:
                return []
            else:
                result.append(temp)
        return result
```

## Time Complexity
O(n*log n)

## Space Complexity

O(n) 
