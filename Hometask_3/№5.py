class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Сохраняем обработанные элементы в хэштаблице. Обращение к ней за О(1), соответсвенно удается обойтись одним циклом
        a = {}
        for i in range(len(nums)):
            if (target - nums[i]) in a:
                return [a[(target - nums[i])], i]
            a[nums[i]] = i
        return []
