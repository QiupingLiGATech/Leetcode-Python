# 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets

## Thoughts and Approaches

To facilitate the two-pointer technique and easily skip identical elements, first sort nums.

Iterate through nums[i]. The problem then transforms into finding nums[j] + nums[k] = -nums[i], which is identical to LeetCode 167. Two Sum II - Input Array Is Sorted.

The problem requires that the answer must not contain duplicate triplets. How do we avoid duplicates?

In the outer loop: If you find that nums[i] == nums[i-1], then any triplet summing to 0 formed by nums[i] and two subsequent numbers could have also been formed identically by nums[i-1]. This would result in duplicates, so when encountering nums[i] == nums[i-1], simply continue.

In the inner loop: When the sum of the three numbers equals 0, to avoid adding the same triplet to the answer, skip any subsequent identical nums[l], afer fixing nums[i]

## Python Code

```Python
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()

        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]: ## outer loop: deduplicate
                continue

            l=i+1
            r=n-1

            while l<r: ## Inner Loop: Two Pointers
                if nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    ans.append([nums[i],nums[l], nums[r]])
                    l+=1 ## want to find other triplets, while nums[i] is fixed
                    while l<r and nums[l]==nums[l-1]: ## ANOTHER INNER MOST LOOP: if it is a duplicate, skip it by moving left pointer
                        l+=1  ## skip it 
        return ans

        ## Think about this special case: nums = [0, 0, 0, 0, 0, 0]
```

## Time Complexity
o(n^2)

## Space Complexity
o(1)
