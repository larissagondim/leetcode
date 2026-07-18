# N-th Tribonacci Number

| Property | Value |
|-------------|-------|
| **Number** | 1137 |
| **Difficulty** | Easy |
| **Link** | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) |
| **Language** | Python |

## Description

The Tribonacci sequence is defined as follows: `T(0) = 0`, `T(1) = 1`, `T(2) = 1`, and `T(n) = T(n-1) + T(n-2) + T(n-3)` for `n >= 3`. Given `n`, return the value of `T(n)`.

## Thought Process

1. **Core Idea**: Same strategy as Fibonacci, but now we keep **three variables** instead of two, since each term depends on the three preceding ones.

2. **Step-by-step**:
   - Initialize `t1 = 0`, `t2 = 1`, `t3 = 1` (the first three terms)
   - Iterate `n` times:
     - Calculate the next one: `aux = t1 + t2 + t3`
     - Slide the window: `t1 = t2`, `t2 = t3`, `t3 = aux`
   - Return `t1`

3. **Analogy with Fibonacci**: It is the same "sliding window" technique — the difference is that the window has a size of 3 instead of 2. The pattern generalizes to any linear recurrence sequence.

4. **Why `t1` is the result**: After n iterations, `t1` contains `T(n)`, following the same logic as Fibonacci.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) |
| **Space** | O(1) — just three variables |
