# 215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

## Thoughts and Approaches

Solution of the K-th largest element:

1. Construct a Min Heap with size K.
   
2. Add elements to the Min Heap one by one.
   
3. When there are K elements in the “Min Heap”, compare the current element with the top element of the Heap:
* If the current element is not larger than the top element of the Heap, drop it and proceed to the next element.
* If the current element is larger than the Heap’s top element, delete the Heap’s top element, and add the current element to the “Min Heap”.

4. Repeat Steps 2 and 3 until all elements have been iterated.


## Python Code

```Python
heap=[]
for num in nums:
    heapq.heappush(heap,num)
    if len(heap)>k:
        heapq.heappop(heap)
return heap[0] ### The top element is the kth largets element, because this is the MIN heap
```

## Time Complexity 
Step 1 and 2 will require O(Klog K) times, if the elements are added one by one to the heap. Step 3 and 4 will require O(log K) time each time
an elements is replaced in the heap. In the worst case, this will be done (N-K) times. Add them up, this will be O(Nlog K) time.

## Space Complexity
O(k). the heap will contain at most k elements at a time. 



