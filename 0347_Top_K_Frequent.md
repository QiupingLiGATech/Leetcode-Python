# 347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Thoughts and Approaches
My strategy is when we add tuples to heap, we add negative to all frequency, so that maximum frequency will be minimum number.

For example, Input: nums = [10,10,20,20,20,30], k = 2

(3, 20) → (-3, 20)
(2, 10) → (-2, 10)
(1, 30) → (-1, 30)
If we add negative to all frequency, min heap will work as a max heap.

Another Approach: Bucket Sort; 
Put in the same bucket, those numbers that appear with the same frequency. 


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

```Python
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### Step 1: Count frequencies and computer max_cnt
        cnt = Counter(nums)
        max_cnt = max(cnt.values())

        ## Step 2: build buckets that contain freq=0 的list, freq=1 的list, freq=2 的list
        ## 把出现次数相同的元素，放到同一个桶里面。  
        buckets = [[] for _ in range(max_cnt + 1)] ## buckets contains a number of lists 
        
        for x, c in cnt.items():
            buckets[c].append(x)

        ## Step 3: 从后向前，return the k most frequent elements.
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            print(i, buckets[i])
            
            for num in buckets[i]:
                result.append(num)
                print(result)
                
                if len(result) == k:
                    return result
```

## Time Complexity
O(nlog n) for heap method ; O(n) for buckets sort

## Space Complexity
o(n)
