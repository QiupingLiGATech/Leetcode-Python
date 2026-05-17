# 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

## Thoughts and Approaches

Sliding Window Approach. Need to figure out the situations when to expand and when to contract. 

## Python Code

```Python

from typing import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = left = 0
        
        myDict = defaultdict(int)  # 维护从 left index 到right index 的字符及其出现次数
        
        right=0

        while right<len(s): ## This is to expand window 
            myDict[s[right]] += 1
            
            while myDict[s[right]] > 1:  # 窗口内有重复字母; Suggests time to CONTRACT WINDOW
                myDict[s[left]] -= 1  # 移除窗口最左端点字母
                left += 1  # 缩小窗口
                
            ans = max(ans, right - left + 1)  # 更新窗口长度最大值
            right+=1 ## Do not forget right+=1

        return ans
```

## Time Complexity

O(2n)=O(n). In the worst case each character will be visited twice by left and right.

## Space Complexity

O(min(m,n))
