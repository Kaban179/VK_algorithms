class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = {}
        ans = []
        for string in strs:
            a.setdefault(''.join(sorted(list(string))), []).append(string)
        for key, value in a.items():
            ans.append(value)
        return ans

    # Сортируем строки, чтобы получить ключи, единые для анаграм. Далее заполняем хэш таблицу, где сортированная строка - ключ, а обычные строки - элементы массива
    # В конце остается только собрать это вместе
