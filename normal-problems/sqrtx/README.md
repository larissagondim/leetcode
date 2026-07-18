# Sqrt(x)

| Property | Value |
|-------------|-------|
| **Number** | 69 |
| **Difficulty** | Easy |
| **Link** | [Sqrt(x)](https://leetcode.com/problems/sqrtx/description/) |
| **Language** | Python |

## Description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.

## Thought Process

### Implemented Solution — built-in `sqrt()`

The direct solution uses `int(sqrt(x))`, taking advantage of Python's built-in math function.

### Alternative Solution (commented) — Binary Search

1. **Core Idea**: The integer square root of `x` is the largest integer `m` such that `m² <= x`. We can find this value using **binary search** in the range `[0, x]`.

2. **Step-by-step**:
   - `left = 0`, `right = x`
   - While `left <= right`:
     - `mid = (left + right) // 2`
     - If `mid * mid <= x` → `mid` is a valid candidate, save it in `ans` and try a larger value: `left = mid + 1`
     - If `mid * mid > x` → `mid` is too large: `right = mid - 1`
   - Return `ans`

3. **Why binary search works here**: The function `f(m) = m²` is monotonically increasing, so the search space satisfies the required property for binary search.

4. **Advantage of binary search**: It doesn't rely on floating-point functions, avoiding precision issues in languages with limited floating-point arithmetic.

## Complexity

| Type | Complexity (Binary Search) |
|------|-------------|
| **Time** | O(log x) |
| **Space** | O(1) |
