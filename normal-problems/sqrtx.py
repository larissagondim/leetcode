import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
    
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         left, right = 0, x
#         ans = 0

#         while left <= right:
#             mid = (left + right) // 2

#             if mid * mid <= x:
#                 ans = mid
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return ans