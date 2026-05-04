# 455 Assign Cookies
[Leetcode Problem](https://leetcode.com/problems/assign-cookies/)

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

## My Thoughts and Solution
We skip a cookie, but we never skip a child; This is a greedy apporach because the current child always receives the cookie, and we never skip a child. 
This is the locally optimal choice. Even though the next child may be saisfied by larger cookies. 

## Code
```Python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort() 
        i=j=0
        count=0
        while i<=len(g)-1 and j<=len(s)-1:
            if s[j]>=g[i]: ###当前小孩可以被满足！！！我们移动到下一个小孩子，移动到下一个Cookie
                count+=1
                j+=1
                i+=1
            else:      ### 当前小孩不可以被满足， 当前小孩子不动， 我们只移动到下一个Cookie 
                j+=1
        return count
```

## Time Complexity

O(n⋅logn+m⋅logm) where n is the size of the array g and m is the size of the array s. Sorting an array of length k takes O(k⋅logk), we need to sort two given arrays. The while loop iterates over each cookie and child once, taking O(m+n). To sum up, the overall time complexity is O(n⋅logn+m⋅logm)

## Space Complexity

O(m+n) In Python, the sort method sorts a list using the Timesort algorithm which is a combination of Merge Sort and Insertion Sort and has O(n+m) additional space

