# 9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

## Thoughts and Approaches

The easiest approach is to convert integer into string, then iterate and compare.

Another more complex approach is through math, to be more specific, via % and //, to get the last digit of x, step by step. 

## Python Code: Approach 1 and Approach 2

```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<=9:
            return True
        x=str(x)
        n=len(x)

        for i in range(n//2):
            if x[i]!=x[n-1-i]:
                return False
        return True
```

```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10 ## get the last digit of x, step by step
            x //= 10 ## get rid of the last digit of x, step by step 
            

        return x == revertedNumber or x == revertedNumber // 10 ## even length vs. odd length
```

## Time Complexity for Approach 2
O(log (n)). We divided the input by 10 for every iteration, so the time complexity is O(log(n))

## Space Complexity for Approach 2
O(1)
