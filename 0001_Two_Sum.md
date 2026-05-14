## 1. Two Sum

[Leetcode Problem](https://leetcode.com/problems/two-sum/description/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


## Thoughts and Approaches

Hash Table; to Improve Time Complexity。 when should we use a hash-based approach? Whenever you need to determine if an element has appeared before, 
or if an element exists within a collection, a hash table should be the very first thing that comes to mind.

## Python Code

```Python
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={}

        for i,x in enumerate(nums):
            hashtable[x]=i ### a hashtable of element and its last occuring index. 
            

        for i, x in enumerate(nums): 
            complement=target-x
            
            if complement in hashtable and i !=hashtable[complement]: ## 当前index不能够等于complement last occuring index
                return [i,hashtable[complement]]
            else:
                continue

        return [] ## if no valid pair is found, return an empty list 
```

## Time Complexity
O(N) We traverse the list exactly twice. Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n)

## Space Complexity
Space Complexity: O(N) This depends on the hash table which stores n elements. 


