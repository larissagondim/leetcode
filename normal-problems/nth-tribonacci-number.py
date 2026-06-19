class Solution:
    def tribonacci(self, n: int) -> int:
        t1 = 0
        t2 = 1
        t3 = 1
        for i in range(n):
            aux = t1 + t2 + t3
            t1 = t2
            t2 = t3
            t3 = aux

        return t1