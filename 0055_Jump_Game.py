#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###要解决“跳跃游戏”，核心思想是贪心算法 (Greedy)：维护一个你当前能到达的最远边界。
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0 ###能够想到max_reach; 而且允许i从每一个index都试一遍，作为起跳点！！！
        n = len(nums)
        
        for i in range(n):
            # 如果当前索引 i 已经超过了你能到达的最远距离，说明卡住了
            if i > max_reach:
                return False
            
            # 更新当前能达到的最远位置
            max_reach = max(max_reach, i + nums[i])
            
            # 如果最远位置已经覆盖了最后一个下标，提前返回 True
            if max_reach >= n - 1:
                return True
                
        return False

###要解决“跳跃游戏”，核心思想是贪心算法 (Greedy)：维护一个你当前能到达的最远边界。
