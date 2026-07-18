# Fibonacci Number

| Property | Value |
|-------------|-------|
| **Number** | 509 |
| **Difficulty** | Easy |
| **Link** | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) |
| **Language** | Python |

## Description

Given `n`, calculate `F(n)`, where `F(n)` is the n-th Fibonacci number. The sequence starts with `F(0) = 0`, `F(1) = 1`, and each subsequent number is the sum of the two preceding ones.

## Thought Process

1. **Core Idea**: Instead of using recursion (which would have exponential complexity without memoization), we use **iterative dynamic programming** with just two variables — we always keep the two previous values.

2. **Step-by-step**:
   - Initialize `f1 = 0` (F(0)) and `f2 = 1` (F(1))
   - Iterate `n` times:
     - Calculate the next one: `aux = f1 + f2`
     - Move forward: `f1 = f2`, `f2 = aux`
   - Return `f1` (which after n iterations contains F(n))

3. **Why return `f1` and not `f2`**:
   - Before the loop: `f1 = F(0)`, `f2 = F(1)`
   - After 1 iteration: `f1 = F(1)`, `f2 = F(2)`
   - After n iterations: `f1 = F(n)`, `f2 = F(n+1)`
   - So `f1` is the correct result

4. **Advantage over recursion**: Simple recursion has O(2ⁿ) time complexity due to recalculating subproblems. This iterative approach solves it in O(n) with O(1) space.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) |
| **Space** | O(1) — just two variables |
