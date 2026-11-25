class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLeft = 0
        maxRight = 0

        def expandAroundCenter(l, r):
            nonlocal maxLeft, maxRight

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Обновляем границы максимального палиндрома
                if r - l > maxRight - maxLeft:
                    maxLeft = l
                    maxRight = r

                l -= 1
                r += 1

        for i in range(len(s)):
            expandAroundCenter(i, i)      # Нечётная длина
            expandAroundCenter(i, i + 1)  # Чётная длина

        return s[maxLeft:maxRight + 1]
