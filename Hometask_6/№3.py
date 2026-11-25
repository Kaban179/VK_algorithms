from typing import List


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]
        
# dp[i] — минимальное количество монет для получения суммы i.
# Если взять монету номиналом coin, то останется набрать
# сумму i - coin, для которой оптимальное решение уже известно.
# Прибавляем 1 за взятую монету.
# Перебираем все допустимые номиналы и выбираем минимум,
# поэтому полученное решение является оптимальным.
