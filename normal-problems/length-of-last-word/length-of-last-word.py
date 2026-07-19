class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = 0
        for char in s[::-1].lstrip():
            if char != ' ':
                size += 1
            else:
                break
        return size