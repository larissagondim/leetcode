# Running Sum of 1d Array

| Property | Value |
|-------------|-------|
| **Number** | 1480 |
| **Difficulty** | Easy |
| **Link** | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/description/) |
| **Language** | Python |

## Description

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`. Return the running sum of `nums`.

## Thought Process

1. **Core Idea**: Modify the array **in-place** — each element accumulates the sum of all preceding ones. Instead of recalculating the sum from zero for each position, we use the fact that `runningSum[i] = runningSum[i-1] + nums[i]`.

2. **Step-by-step**:
   - The first element is already its own running sum
   - From index 1 onwards: `nums[i] += nums[i-1]`
   - This transforms each position into the accumulated sum up to that point
   - Return the modified array

3. **Example**: `[1, 2, 3, 4]`
   - `i=1`: `nums[1] = 2 + 1 = 3` → `[1, 3, 3, 4]`
   - `i=2`: `nums[2] = 3 + 3 = 6` → `[1, 3, 6, 4]`
   - `i=3`: `nums[3] = 4 + 6 = 10` → `[1, 3, 6, 10]`

4. **Concept**: This is the **prefix sum** operation, which is fundamental in many algorithms and competitive programming problems.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — one pass through the array |
| **Space** | O(1) — in-place modification |
