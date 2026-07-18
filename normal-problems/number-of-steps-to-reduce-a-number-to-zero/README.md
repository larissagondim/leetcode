# Number of Steps to Reduce a Number to Zero

| Property | Value |
|-------------|-------|
| **Number** | 1342 |
| **Difficulty** | Easy |
| **Link** | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/) |
| **Language** | Python |

## Description

Given an integer `num`, return the number of steps to reduce it to zero. In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

## Thought Process

1. **Core Idea**: Directly simulate the described process — it is a **direct simulation** problem. At each step, we apply the corresponding rule and count.

2. **Step-by-step**:
   - Initialize the operations counter `op = 0`
   - While `num != 0`:
     - If `num` is **even** (`num % 2 == 0`): divide by 2
     - If `num` is **odd**: subtract 1
     - Increment `op` in both cases
   - Return `op`

3. **Example**: `num = 14`
   - 14 → even → 7 (1 step)
   - 7 → odd → 6 (2 steps)
   - 6 → even → 3 (3 steps)
   - 3 → odd → 2 (4 steps)
   - 2 → even → 1 (5 steps)
   - 1 → odd → 0 (6 steps)

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(log n) — each division by 2 reduces the number by half |
| **Space** | O(1) — only auxiliary variables |
