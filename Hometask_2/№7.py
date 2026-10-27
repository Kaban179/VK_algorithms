class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Медленный указатель всегда указывает на следующее место уникального элемента. Быстрый бежит дальше, и если находит новый элемент, ставит его на место, где стоит первый
        # Если элемент не новый, то просто превращаем его в _. В конце эти элементы окажутся в конце списка
        i = 0
        j = 0
        count = 0
        last_elem = -1000
        while j < len(nums):
            if nums[j] != last_elem:
                last_elem = nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
                count += 1
            else:
                nums[j] = '_'
                j += 1
        return count
