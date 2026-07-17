# 6 ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

## Thoughts and Approaches

We first initialize the result as a list of empty string, one empty string for each row. Then we need to decide move ups and move downs. In this solution, we introduced flag and used "i+=flag" to determine the value of i . Flag can be either 1 (moving down rows) or -1 (moving up rows). When we hit the very top row, so we must start moving down (flag becomes 1). When i == numRows - 1, we've hit the bottom row, so we must start moving up (flag becomes -1).

## Python Code

```Python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: 
            return s
        res = ["" for _ in range(numRows)] ## initialize a list of empty strings, number of empty strings=number of rows. 

        
        i, flag = 0, 0 ##flag is a direction switcher. When flag = 1, adding it to i moves you down to the next row (0 -> 1 -> 2). ## when flag=-1, adding it to i moves you up. 
        
        for c in s: ## Traverse every character in string. 

            res[i] += c ##append this character to the string at the right row. 
            
            
            if i == 0:  ## top row:  I should go down to the next row
                flag=1
                
            if i==numRows-1: ## bottom row: I should go up to the next row.
                flag=-1
            
                
            i += flag
            
        return "".join(res) ## join all strings together. 

```

## Time Complexity
O(n)

## Space Complexity
O(n) 
