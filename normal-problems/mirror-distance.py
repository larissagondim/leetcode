class Solution:
    def mirrorDistance(self, n: int) -> int:
        aux = n
        rev = 0

        while aux > 0:
            rev = rev * 10 + aux % 10
            aux //= 10

        return abs(rev - n)