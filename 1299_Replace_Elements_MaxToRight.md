# 1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

## Thoughts and Approaches

Loop through the array starting from the end. Keep the maximum value seen so far. Do Not Forget to Save the ARR[I], otherwise, it will be overwritten.

## Python Code

```Python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        maxRight=arr[n-1]
        for i in range(n-2,-1,-1):
            temp=arr[i] ## The most critical line: to save the arr[i] to temp
            arr[i]=maxRight ## rewrite 改写 arr[i]
            maxRight=max(temp,maxRight) ## update maxRight, including original value temp

        arr[n-1]=-1

        return arr
```

## Time Complexity

O(n)

## Space Complexity

O(1) 
