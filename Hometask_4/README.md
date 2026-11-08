# Домашнее задание 4

Файлы с задачами содержат только сигнатуры методов и `pass`: решения добавляются самостоятельно.

## Соответствия LeetCode

1. Восстановление бинарного дерева из level-order массива. Точного аналога с таким входом нет: в LeetCode level-order обычно используется для сериализации/примеров, а не как отдельная задача на построение. Метод `buildTree(values)` принимает список значений уровнями; `None` обозначает отсутствующего узла.
2. Симметрия дерева — [LeetCode 101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree/). Метод `isSymmetric(root)`.
3. Минимальная глубина дерева — [LeetCode 111: Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/). Метод `minDepth(root)`.
4. Произведение минимума и максимума в BST, заданном массивом. Точного аналога на LeetCode нет. `minMaxProduct(values)` принимает BST в level-order представлении; `None` — отсутствующий узел. Для пустого дерева в тестах ожидается `0`.
5. Идентичность двух деревьев — [LeetCode 100: Same Tree](https://leetcode.com/problems/same-tree/). Метод `isSameTree(p, q)`.

## Тесты

Запуск из корня репозитория: `python -m pytest Hometask_4/tests`

Первый аплоад заготовок и тестов может быть сделан для удобства нейросетью. Нейросети для решения задач нигде не используются.
