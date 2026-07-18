# Find Numbers with Even Number of Digits

| Property | Value |
|-------------|-------|
| **Number** | 1295 |
| **Difficulty** | Easy |
| **Link** | [Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/) |
| **Language** | Python |

## Description

Given an array `nums` of integers, return how many of them contain an **even** number of digits.

## Thought Process

1. **Core Idea**: To count the digits of a number, we just need to convert it to a string and check its length. If the length is even, we increment the counter.

2. **Step-by-step**:
   - Initialize a counter `even = 0`
   - For each number in the array:
     - Convert to string: `str(nums[i])`
     - Check if the length is even: `len(str(nums[i])) % 2 == 0`
     - If yes, increment `even`
   - Return `even`

3. **Alternative approach**: We could count digits mathematically (by repeatedly dividing by 10), but string conversion is more readable and equally efficient for the problem constraints.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n × d) — where d is the average number of digits |
| **Space** | O(d) — for the string conversion |
