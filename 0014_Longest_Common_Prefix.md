# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Thoughts and Approaches

Compare character-by-character from top to bottom. Look at the first character of all strings, then the second character of all strings, and so on.

## Python Code

```Python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference=min(strs,key=len)
        n=len(reference)

        for i in range(n):  ## o(m)
            for x in strs: ### o(n)
                if x[i]==reference[i]:
                    continue
                else: 
                    return reference[:i] ## note there is only 1 colon
                    
        return reference
```

## Time Complexity
o(N*M) where n is the length of the shortest string, and m is the length of strs.

## Space Complexity
o(1) We only used constant extra space. 
