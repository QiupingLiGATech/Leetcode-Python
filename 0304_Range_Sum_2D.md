# 304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.


## Thoughts and Appraoches

1. Initialization: Computing the 2D Prefix Sum
In the prefix sum matrix s, the element s[i + 1][j + 1] represents the total sum of all elements in the original matrix from the top-left corner (0, 0) down to the bottom-right corner (i, j).

To prevent index-out-of-bounds errors (for instance, when handling the 0th row or 0th column), the code intentionally allocates an extra row and column, making the size of the prefix sum matrix (m + 1) * (n + 1), padded with 0s by default.

Deriving the Recurrence Relation:

s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + a[i][j]


2. Calculating the Submatrix Region Sum
   
When sumRegion(r1, c1, r2, c2) is called to get the sum of the region from (r1, c1) to (r2, c2), the code uses this formula:
return s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1]

## Python Code

```Python
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)] ## s 初始化成为一共（m+1)行， 一共（n+1) 列；
        for i, row in enumerate(matrix): ## 这样摘出来each row; 
            for j, x in enumerate(row): ## 这样子摘出来each element x in ith row, and jth colum in the matrix
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s #在前缀和矩阵 s 中，s[i + 1][j + 1] 代表原矩阵从左上角 (0, 0) 到右下角 (i, j) 这个矩形范围内所有元素的总和。

    # 返回左上角在 (r1, c1) 右下角在 (r2, c2) 的子矩阵元素和
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        s = self.s
        return s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

## Time Complexity

O(mn) for initialization, only needs to be computed once when object is created; 
O(1) for computing sumRegion, where m and n are the number of rows and columns of the matrix, respectively.

## Space Complexity
o(mn) during initialization. 
