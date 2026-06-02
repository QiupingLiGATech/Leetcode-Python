# 347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Thoughts and Approaches
My strategy is when we add tuples to heap, we add negative to all frequency, so that maximum frequency will be minimum number.

For example, Input: nums = [10,10,20,20,20,30], k = 2

(3, 20) → (-3, 20)
(2, 10) → (-2, 10)
(1, 30) → (-1, 30)
If we add negative to all frequency, min heap will work as a max heap.


## Python Code
```Python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        heap=[]
        counter={}
        for n in nums:                        ## O(n) time complexity
            counter[n]=1+counter.get(n,0)
            
        for key, val in counter.items():      ## O(nlog n) 
            heapq.heappush(heap, (-val,key))  ##
        
        res=[]
        while len(res)<k:                       ## O(klog n) 
            res.append(heapq.heappop(heap)[1])
        return res
```

## Time Complexity
O(nlog n)

## Space Complexity
o(n)
