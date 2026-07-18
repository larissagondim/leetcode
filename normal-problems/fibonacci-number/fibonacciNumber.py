class Solution:
    def fib(self, n: int) -> int:
        f1 = 0
        f2 = 1
        for i in range(n):
            aux = f1 + f2
            f1 = f2
            f2 = aux        

        return f1