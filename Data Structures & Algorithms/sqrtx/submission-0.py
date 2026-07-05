class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x
        sqrt = None

        while s <= e:
            m = (s + e) // 2
            if m*m == x:
                return m
            elif x < m*m:
                e = m - 1
            elif x > m*m:
                s = m + 1
        

        return e