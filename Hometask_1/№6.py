def even_first(nums: list[int]) -> None:
    pos = 0  # Позиция для следующего чётного числа

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even = nums[i]

            # Сдвигаем элементы вправо, сохраняя их порядок
            for j in range(i, pos, -1):
                nums[j] = nums[j - 1]

            nums[pos] = even
            pos += 1

    # Порядок сохраняется, так как чётные числа обрабатываются
    # слева направо, а остальные элементы только сдвигаются.
    # Время: O(n²), память: O(1).
