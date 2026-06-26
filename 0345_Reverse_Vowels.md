# 345 Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

## Thoughts and Approaches
The key part is to convert string to a list; then at the end, convert list to a string; becasue String does not allow character swapping; while list allows character swapping.

## Python Code
```Python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel={"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} ## initialize a set with values
        n=len(s)
        # Convert the string to a list to allow item assignment
        sList = list(s)
        i=0
        j=n-1

        while i<j: 
            if sList[i] in vowel and sList[j] in vowel:  ## hashset lookup time: O(1)
                sList[i],sList[j]=sList[j],sList[i]
                i+=1
                j-=1
            elif sList[i] in vowel and sList[j] not in vowel:
                j-=1
            elif sList[i] not in vowel and sList[j] in vowel: 
                i+=1
            else: ## this case: s[i] not in vowel and s[j] not in vowel
                i+=1
                j-=1
        return "".join(sList)
```

## Time Complexity
O(n) because hash set lookup takes only O(1) time

## Space Complexity
O(n) when you create a list and also create a final string. O(n) + O(n) 
