# 8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.


## Thoughts and Approaches

There is a critical step here to assemble the final integer:  number = number * 10 + int(s[i]) ## read each number one by one 

## Python Code

```Python
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        # 跳过前导空格
        i = 0
        while i <= n-1 and s[i] == ' ':
            i += 1

        # 处理正负号
        sign = 1
        if i <= n-1 and s[i] in "+-":
            sign = 1 if s[i] == '+' else -1
            i += 1

        # 处理数字
        MAXBOUND = 2**31 - 1
        number = 0

        while i <= n-1 and '0' <= s[i] <= '9':
            number = number * 10 + int(s[i]) ## read each number one by one，from the first number to the last number; number=0, 1, 10+3, 13*10+3, 133*10+7
            
            if number > MAXBOUND:  # 最终答案已确定，提前返回
                return MAXBOUND if sign > 0 else -2**31
            i += 1

        return sign * number
```

## Time Complexity
O(n)

## Space Complexity
O(1) 
