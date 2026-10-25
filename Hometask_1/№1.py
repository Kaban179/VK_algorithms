def rotate(self, nums: list[int], k: int) -> None:
        #Решение имеет линейную сложность, так как проходимся 3 разу по массиву и каждый проход ключает в себя n или меньше итераций. То есть сложность = O(3n) = O(n). Дополнительная память не выделяется
        k = k % len(nums)
        
        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left = 0
        right = k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        left = k
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

        """
        Do not return anything, modify nums in-place instead.
        """
