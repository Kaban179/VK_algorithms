from typing import Optional, List

class Solution:
    def minMaxProduct(self, values: List[Optional[int]]) -> int:
        if len(values) < 3:
            return -1

        # Ищем минимальный элемент (идём всегда влево)
        min_index = 0
        while 2 * min_index + 1 < len(values):
            next_index = 2 * min_index + 1
            if values[next_index] is None:
                break
            min_index = next_index

        # Ищем максимальный элемент (идём всегда вправо)
        max_index = 0
        while 2 * max_index + 2 < len(values):
            next_index = 2 * max_index + 2
            if values[next_index] is None:
                break
            max_index = next_index

        return values[min_index] * values[max_index]

#Каждый из элементов мы находим за O(h), потому что просто спускаемся по дереву вниз
