## 58 Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

## Thoughts and Approaches

Use Python built in function

## Python Code

```Python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        return len(x[-1])

```

## Time Complexity
O(N)

# Space Complexity
o(n)
