# 55. Jump Game (跳跃游戏)

### 题目描述
给定一个非负整数数组 `nums` ，你最初位于数组的第一个下标。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个下标。

### 我的思考与解题思路
这道题的核心思想是 **贪心算法 (Greedy)**。

1. **关键变量**：我们需要维护一个变量 `max_reach`，代表当前我们能够到达的最远边界。
2. **全局视角**：不再纠结于具体的某一次跳跃，而是允许 `i` 遍历每一个索引（每一个 index 都试一遍），把每一个位置都作为“起跳点”。
3. **动态更新**：
   - 如果当前位置 `i` 还没超过 `max_reach`，说明我们可以到达这里。
   - 在每一个能到达的位置，我们更新 `max_reach = max(max_reach, i + nums[i])`。
   - 一旦 `max_reach` 覆盖了最后一个下标，就成功了。
   - 如果在中间某个点 `i` 超过了 `max_reach`，说明我们卡住了（遇到了 0 且跳不过去），返回 `False`。

### 代码实现 (Python)

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0 # 能够想到 max_reach 是解题的关键
        n = len(nums)
        
        # 遍历每一个 index，将其作为起跳点尝试
        for i in range(n):
            # 如果当前索引 i 已经超过了你能到达的最远距离，说明中间有“坑”跳不过去了
            if i > max_reach:
                return False
            
            # 更新当前能达到的最远位置
            max_reach = max(max_reach, i + nums[i])
            
            # 如果最远位置已经覆盖了最后一个下标，提前返回 True
            if max_reach >= n - 1:
                return True
                
        return False
```

### 复杂度分析
时间复杂度: O(n)，只需要遍历一次数组。    
空间复杂度: O(1)，只使用了常数级别的额外空间。
