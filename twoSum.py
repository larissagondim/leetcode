class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {nums[i]: i for i in range(len(nums))}  
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict and dict[complement] != i:
                return [dict[complement], i]
