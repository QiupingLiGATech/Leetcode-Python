# 204 Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

## Thoughts and Approaches

Instead of asking "Is this individual number prime?" n times, we ask "Which numbers here are composite?" once. This is a Sieve approach.

The Core Idea: We assume all numbers up to n are prime initially. We start at the first prime 2 and cross out all of its multiples (4, 6, 8, ...). 
Then we move to the next unmarked number (3) and cross out all of its multiples. Repeat until we reach sqrt(n); 

why reach sqrt(n): Any composite number N must have a factor less than or equal to sqrt{N}.

why inner loop start with num^2: When marking multiples of a prime i, we don't need to start at $2i, 3i, \dots$. Those have already been marked by smaller prime factors. We can safely start marking at i*i

## Python Code 
```Python
class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosethenes
        ## we only consider the multiples of primes numbers 
        if n<=2:
            return 0
        CheckList=[True]*n ## by default, every number from 0 to n-1 is prime number
        CheckList[0]=False
        CheckList[1]=False

        
        ## General case: check each numer is prime or not
        for num in range(2,int(n**0.5)+1):  ##外层循环只需到 qrt{n}：因为如果一个合数可以分解为 p*q，那么 p 和 q 之中一定有一个小于或等于 sqrt{n}。

            if CheckList[num]: ## if num is a prime number
                for indx in range(num*num, n, num): ###内层循环从 num*num 开始，比如当 i = 3 时，我们不需要从 3*2 = 6 开始标记，因为 2*3在之前 i = 2 的时候已经被标记过了。所以直接从 3*3 = 9 开始标记即可。

                    CheckList[indx]=False
        
        return sum(CheckList)
```

## Time Complexity
O(nloglogn)

## Space Complexity
O(n) 




