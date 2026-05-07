# 763 Partition Labels
[Leetcode题目](https://leetcode.com/problems/partition-labels/description/）

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

## Thoughts and Appraoches

To ensure a character like 'a' only appears in one partition, that partition must extend at least to the very last occurrence of 'a' in the string.

Find Last Occurrences: First, scan the string to record the last index where every character appears.

Determine Boundaries: Iterate through the string again. Keep track of the "furthest point" needed to satisfy all characters encountered so far.

Cut the String: When your current index reaches that "furthest point," you’ve found a valid partition.

### Where is the difficulty? Update the Partition Boundary!

To satisfy the problem's constraint (that a letter can only appear in one chunk), a partition must be at least long enough to include the very last appearance of every character within it.

How it works step-by-step
Imagine you are walking down the string from left to right:

Encountering a character: Every time you step on a character, you look up its "final exit" (the last_occurrence).

Evaluating the boundary: You ask yourself: "Does this new character I just found stay within my current boundary, or does it force me to go further?"

Updating the end: The max() function ensures that your current partition boundary (end) only moves forward. It will never shrink. It stretches to accommodate the "latest" last occurrence seen so far.

```Python
def partitionLabels(s: str) -> list[int]:
    
    last_occurrence = {char: i for i, char in enumerate(s)} ###Dictionary Comprehension # Step 1: Record the last index of each character
    
    result = []
    start = 0  ## start is the left boundary
    end = 0  ## end is the right boundary
    
    for i, char in enumerate(s):  # Step 2: Iterate to find partitions

        end = max(end, last_occurrence[char])  # The VIP LINE: Update the end of the current partition to the furthest last occurrence of any character seen so far
        
        
        if i == end:         # # If the current index matches the furthest last occurrence, We found a partition! Calculate length and store it
            result.append(i - start + 1) ## update the result 
            start = i + 1    # Move the start to the next character
            
    return result

```

## Time Complexity
O(n)

# Space Complexity
O(1) 
