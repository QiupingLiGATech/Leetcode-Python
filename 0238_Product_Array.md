# Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Thoughts and Apporaches

answer[i] is equal to the product of all elements in nums except nums[i]. In other words, if we know the product of all elements to the left of index i and the product of all elements to the right of index i, we can compute answer[i].

Therefore:

Let pre[i] denote the product of elements from nums[0] to nums[i-1].
Let suf[i] denote the product of elements from nums[i+1] to nums[n-1].

We can compute pre[i] incrementally. If we already know the product of elements from nums[0] to nums[i-2], namely pre[i-1], then multiplying it by nums[i-1] gives pre[i]:

pre[i]=pre[i−1]×nums[i−1]

Similarly,

suf[i]=suf[i+1]×nums[i+1]
Initialization

Set:

pre[0] = 1
suf[n-1] = 1

According to the definitions above, both pre[0] and suf[n-1] represent the product of an empty subarray. We define the product of an empty subarray to be 1, since multiplying any number x by 1 leaves it unchanged. This convention also makes it convenient to compute pre[1], suf[n-2], and the remaining values using the recurrence relations.

Once the pre and suf arrays have been computed, the answer for each index is simply:

answer[i]=pre[i]×suf[i]

## Python Code
```Python
lass Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n  ##前缀乘机：定义 pre[i] 表示从 nums[0] 到 nums[i−1] 的乘积。
        for i in range(1, n):                   ## pre[i]=nums[0]*...*nums[i-2]*nums[i-1]
            pre[i] = pre[i - 1] * nums[i - 1]  ## pre[i-1]=nums[0]*...*nums[i-2]

        suff = [1] * n ## 后缀乘机： 定义 suff[i] 表示从 nums[i+1] 到 nums[n−1] 的乘积。
        for i in range(n - 2, -1, -1): ## suff[i]=nums[i+1]*nums[i+2]...*nums[n-1]
            suff[i] = suff[i + 1] * nums[i + 1] ## suff[i+1]=nums[i+2]*...*nums[n-1]

        answer=[1]*n
        
        for i in range(n):
            answer[i] = pre[i] * suff[i]

        return answer

```

## Time Complexity
O(N): go through the list 3 times

## Space Complexity
O(N) 
