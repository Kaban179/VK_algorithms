# Домашнее задание 5

В файлах `№1.py`–`№6.py` находятся структуры узлов и сигнатуры функций. Реализации намеренно оставлены пустыми (`pass`).

## Задачи и соответствия LeetCode

1. Проверка полноты бинарного дерева — [LeetCode 958: Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/). Метод `isCompleteTree(root)`.
2. Слияние K отсортированных массивов с помощью min-heap. Близкая задача — [LeetCode 23: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/), где сливаются связанные списки, а здесь — массивы. Метод `mergeKArrays(arrays)`.
3. K-й наименьший и K-й наибольший элементы массива — [LeetCode 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/). Добавлены методы `findKthLargest(nums, k)` и `findKthSmallest(nums, k)`; при равных значениях порядок учитывает повторы, как в условии LeetCode.
4. K-й наименьший и K-й наибольший элементы BST. Для наименьшего есть [LeetCode 230: Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/); наибольший — симметричный вариант обхода в обратном порядке. Методы `kthSmallest(root, k)` и `kthLargest(root, k)`.
5. Вычисление `balance_factor` для каждого узла BST. Точного соответствия LeetCode нет; близкая задача о высотной сбалансированности — [LeetCode 110: Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/), но она возвращает булево значение, а не заполняет баланс-факторы. `balance_factor` определяется как `height(left) - height(right)`. Метод `calculateBalanceFactors(root)` записывает его в поле каждого узла; высота пустого поддерева в тестах принята равной 0.
6. Преобразование дерева в зеркальное — [LeetCode 226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/). Метод `invertTree(root)`.

## Тесты

Из корня репозитория: `python -m pytest Hometask_5/tests`

Первый аплоад файлов и тестов может быть выполнен нейросетью для удобства. Нейросети для решения задач не используются.
