class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # low — граница нулей, mid — текущий элемент, high — граница двоек.
        # Нули переносим в начало, двойки — в конец, единицы оставляем.
        # При обмене с high не двигаем mid, так как новый элемент ещё не проверен.
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
             
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        
