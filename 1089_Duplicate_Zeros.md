# 1089 Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]


## Thoughts and Apporaches

Instead of shifting elements repeatedly (which is slow) or using a second array (which takes extra memory), this approach uses two pointers in two distinct phases:

Pass 1: Forward Scan (Planning)  ---> [ Find last surviving index & Zero Count ]
Pass 2: Backward Scan (Writing) <--- [ how to map the value from the read pointer to the write pointer] 
The reason we shift backwards is the golden rule of in-place array manipulation: You must never overwrite data before you have a chance to read it. 
If you try to shift elements forward (from left to right) inside the same array, you will instantly cause a chain reaction that destroys your original data.


## Python Code

```Python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = 0
        last_surviving_index = n - 1

        # Pass 1: Find the true cutoff boundary and valid zero count
        for i in range(n):
            if i > last_surviving_index: ## boundary check: exceeded the boundary, break the loop 
                break
            if arr[i] == 0:
                # Edge case: Zero lands exactly on the last boundary spot.
                # It can be copied, but there's no room to duplicate it.
                if i == last_surviving_index:
                    arr[n - 1] = 0
                    last_surviving_index -= 1
                    break
                zeros += 1 ## zeros: up to index i, including i, 需要【额外插队加塞】的0的数量。 
                last_surviving_index -= 1 #如果0的数量+1， 那么last suriving index 就要-1

        # Pass 2: Clean, guard-free backward shifting 
        ## two pointers: read pointer i, write pointer i+zeros
        for i in range(last_surviving_index, -1, -1):
            if arr[i] == 0:
                arr[i + zeros] = arr[i] ## value 被map 了
                arr[i + zeros-1] = 0 ## 我增加了1个0
                zeros-=1  ##zeros: 前面up to index i, including i, 需要【额外插队加塞】的0的数量。 
            else:
                arr[i + zeros] = arr[i] ## value 被map 了

```

## Time Complexity
O(n); Just two passes. 

## Space COmplexity
O(1) 
