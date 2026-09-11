class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDouble = False
        frequencia = {}
        for num in nums:
            frequencia[num] = frequencia.get(num, 0) + 1
            if frequencia[num] > 1:
                isDouble = True
                break
        return isDouble


        