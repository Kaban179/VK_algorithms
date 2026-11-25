from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

# Если текущий элемент больше предыдущего, увеличиваем длину на 1
# Иначе оставляем длину равной 1
# Временная сложность — O(n), так как проходим массив один раз.
# Пространственная сложность — O(1).
