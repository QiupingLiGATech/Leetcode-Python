# 1. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

## Thoughts and Approaches

The main difficulty of this problem lies in handling the six special cases. However, these six cases can actually be unified:Let x = s[i] and y = s[i+1], 
representing two adjacent Roman numerals.If the value of x is less than the value of y, then the value of x should be taken as its negative. 
For example, the "I" in "IV" is equivalent to -1, and the "C" in "CM" is equivalent to $-100.
Finally, sum up all the values to get the answer.

## Python Code

```Python
class Solution:
    def romanToInt(self, s: str) -> int:
        myDict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result=0
        n=len(s)
        i=0

        while i<=n-1:  ## i is index 
            ## Step 1: ALWAYS FIRST Examine whether this is the subtractive case
            if i+1<=n-1 and myDict[s[i]]<myDict[s[i+1]]: ## e.g., "IV"
                result+=myDict[s[i+1]]-myDict[s[i]] ## Note: the key=s[i] not i
                i+=2
            else:
                result+=myDict[s[i]]
                i+=1
        return result 
```

## Time Complexity
o(n)

## Space Complexity
O(1)
