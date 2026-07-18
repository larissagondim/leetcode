# Fizz Buzz

| Property | Value |
|-------------|-------|
| **Number** | 412 |
| **Difficulty** | Easy |
| **Link** | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/description/) |
| **Language** | Python |

## Description

Given an integer `n`, return a string array answer (1-indexed) where for each number from 1 to n: if divisible by 3 and 5 → `"FizzBuzz"`, if only by 3 → `"Fizz"`, if only by 5 → `"Buzz"`, else → the number itself as a string.

## Thought Process

1. **Core Idea**: Direct simulation with chained conditionals. The order of the checks is important — we must check **divisibility by both (3 and 5)** first.

2. **Step-by-step**:
   - Create an array of empty strings of size `n`
   - Iterate from 1 to n (inclusive):
     - `i % 3 == 0 AND i % 5 == 0` → `"FizzBuzz"`
     - `i % 3 == 0 AND i % 5 != 0` → `"Fizz"`
     - `i % 3 != 0 AND i % 5 == 0` → `"Buzz"`
     - Else → `str(i)`
   - We use `arr[i-1]` because the array is 0-indexed but we iterate from 1

3. **Why check both first**: If we checked `% 3` earlier, the number 15 would fall into `"Fizz"` and never reach `"FizzBuzz"`. The joint check must have priority.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — we iterate from 1 to n |
| **Space** | O(n) — the result array |
