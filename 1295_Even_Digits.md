# 1 Find Number with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.

## Python Code

```Python
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for x in nums: ## o(n)
            count=1
            
            while x//10>=1: ## o(log(m))
                count+=1
                x=x//10
                

            if count%2==0:
                even+=1

        return even 


```

## Time Complexity

O(nLog m)

## Space Complexity

O(1) 
