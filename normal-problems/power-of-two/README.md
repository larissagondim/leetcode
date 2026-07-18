# Power of Two

| Property | Value |
|-------------|-------|
| **Number** | 231 |
| **Difficulty** | Easy |
| **Link** | [Power of Two](https://leetcode.com/problems/power-of-two/description/) |
| **Language** | Python |

## Description

Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

## Thought Process

1. **Core Idea**: Use **bit manipulation**. Powers of 2 in binary have a special property: they have exactly **one single 1 bit**. For example:
   - `1 = 0001`, `2 = 0010`, `4 = 0100`, `8 = 1000`

2. **The `n & (n - 1)` trick**:
   - If `n` is a power of 2: `n` has a single 1 bit, and `n - 1` has all bits to the right of that 1 turned on
   - Example: `n = 8 (1000)`, `n - 1 = 7 (0111)` → `n & (n - 1) = 0000`
   - If `n` is **not** a power of 2: `n & (n - 1) != 0`
   - Example: `n = 6 (0110)`, `n - 1 = 5 (0101)` → `n & (n - 1) = 0100 ≠ 0`

3. **Complete condition**: `n > 0 and (n & (n - 1)) == 0`
   - `n > 0` excludes zero and negatives (which are not powers of 2)

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(1) — constant bitwise operation |
| **Space** | O(1) |
