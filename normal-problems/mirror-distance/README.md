# Mirror Distance

| Property | Value |
|-------------|-------|
| **Difficulty** | Easy |
| **Link** | [LeetCode](https://leetcode.com/) |
| **Languages** | Python, C |

## Description

Given an integer `n`, calculate the absolute difference between `n` and its reverse (the number with its digits reversed).

## Thought Process

1. **Core Idea**: Reverse a number digit by digit using mathematical operations (modulo and integer division), then calculate the absolute difference.

2. **Step-by-step**:
   - Save the original value in `aux`/`temp`
   - Initialize `rev = 0`
   - While `aux > 0`:
     - Extract the last digit: `aux % 10`
     - Add to the reversed number: `rev = rev * 10 + (aux % 10)`
     - Remove the last digit: `aux //= 10`
   - Result: `abs(rev - n)`

3. **Example**: `n = 123`
   - Iteration 1: `rev = 0 * 10 + 3 = 3`, `aux = 12`
   - Iteration 2: `rev = 3 * 10 + 2 = 32`, `aux = 1`
   - Iteration 3: `rev = 32 * 10 + 1 = 321`, `aux = 0`
   - Result: `|321 - 123| = 198`

4. **Both solutions (Python and C)** follow the same logic, with the difference that in C we use `abs()` from `stdlib.h`.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(d) — where d is the number of digits |
| **Space** | O(1) — only auxiliary variables |
