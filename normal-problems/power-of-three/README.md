# Power of Three

| Property | Value |
|-------------|-------|
| **Number** | 326 |
| **Difficulty** | Easy |
| **Link** | [Power of Three](https://leetcode.com/problems/power-of-three/description/) |
| **Language** | Python |

## Description

Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.

## Thought Process

1. **Core Idea**: Repeatedly divide by 3. If `n` is a power of 3, successive division by 3 will eventually reach 1. If at any point the remainder is not 0, it is not a power of 3.

2. **Step-by-step**:
   - If `n <= 0` → return `False` (powers of 3 are always positive)
   - While `n > 1`:
     - If `n % 3 != 0` → not divisible by 3 → return `False`
     - Otherwise: `n //= 3` (divide by 3)
   - If it exits the loop, `n == 1` → it is a power of 3

3. **Example**: `n = 27`
   - 27 % 3 == 0 → n = 9
   - 9 % 3 == 0 → n = 3
   - 3 % 3 == 0 → n = 1
   - n == 1 → `True` ✓

4. **Contrast with Power of Two**: For power of 2, we use bit manipulation (more efficient). For power of 3, there is no similar bitwise trick, so iterative division is the standard approach.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(log₃ n) — we divide by 3 at each iteration |
| **Space** | O(1) |
