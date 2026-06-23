class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for sublist in grid:
            for num in sublist:
                if num < 0:
                    count += 1
        return count