class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #Записывая элементы с конца мы всегда будем писать либо в нулевые, либо в уже обработанные ячейки. 
        #В каждый момент количество доступных позиций справа не меньше количества элементов, которые мы ещё должны туда записать. Поэтому при выборе наибольшего элемента мы не затрагиваем необработанные данные.
        i = m - 1
        j = n - 1
        k = n + m - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
