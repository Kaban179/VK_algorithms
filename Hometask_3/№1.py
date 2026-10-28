class Solution:
    def mySqrt(self, x: int) -> int:
        # На каждом шаге отбрасываем примерно половину диапазона,
        # поэтому сложность по времени O(log n).
        # Дополнительная память O(1), так как используем только переменные.
        
        l = 0
        r = x
       
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
