from typing import List


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                row.append(1)
            dp.append(row)
        
        for row in range(1, numRows):
            for col in range(1, row):
                dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]
        
        return dp
# Первый и последний элементы каждой строки равны 1.
# Каждый внутренний элемент вычисляется как сумма двух жлементов строки
# Временная сложность — O(n^2), так как всего n(n+1)/2 элементов.
# Пространственная сложность — O(n^2) для хранения треугольника.
