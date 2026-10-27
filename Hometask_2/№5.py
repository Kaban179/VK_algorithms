class Solution:
    def twoSum(self, numbers: list[int], target: int) -> bool:
        # Если не хватает до таргета, значит нужно увеличивать сумму -> двигаем первый указатель. Иначе, правый влево, так чтобы сумма уменьшалась
        # В какой-то момент попадем точно в нужный таргет
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return True
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

        return False
        
        # O(n) по времени: на каждом шаге один из указателей
        # сдвигается к центру, всего не более n-1 шагов.
        # O(1) по памяти: используем только два указателя.
