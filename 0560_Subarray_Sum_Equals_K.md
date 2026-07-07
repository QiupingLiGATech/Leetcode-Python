# 560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

## Thoughts and Approaches

Let's review the definition of the prefix sum from Problem 303:
s[0] = 0, 
and s[i] = nums[0] + nums[1] + ... + nums[i-1].

Note that s is an array of length n + 1, where the first element is 0.

Let i < j. If the sum of elements from nums[i] to $nums[j-1] equals k, expressed in terms of the prefix sum, it becomes s[j] - s[i] = k

Thus, the problem transforms into:How many pairs of indices (i, j) exist in s such that  i < j  and s[j] - s[i] = k

Rewriting it as s[j] + (-s[i]) = k makes it even clearer. This brings us right back to Two Sum.

## Python Code

```Python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        cnt = defaultdict(int)
        ans = 0

        ### 前缀和+哈希表
        ###s[i]=s[j]−k; 如果我们把 s[j]−s[i]=k 移项，得

        for sj in s:
            temp = cnt[sj - k] ## temp: 去历史记录中查找，在当前位置之前，有多少个位置的前缀和恰好等于 sj - k
            ans+=temp   ##每当我们在左边找到一个值等于 s[j]−k 的前缀和，就找到了一个和为 k 的子数组（因为 s[j]−s[i]=k）
            cnt[sj] += 1 

        return ans
```

## Time Complexity
O(n)

## Space COmplexity
O(n) 
