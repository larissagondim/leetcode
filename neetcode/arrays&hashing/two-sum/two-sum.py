class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {nums[i]: i for i in range(len(nums))}  
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict and dict[comp] != i:
                return [i, dict[comp]]
        