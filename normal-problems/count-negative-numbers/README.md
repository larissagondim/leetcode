# Count Negative Numbers in a Sorted Matrix

| Property | Value |
|-------------|-------|
| **Number** | 1351 |
| **Difficulty** | Easy |
| **Link** | [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/) |
| **Language** | Python |

## Description

Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return the number of **negative** numbers in `grid`.

## Thought Process

1. **Core Idea**: **Brute force** approach — iterate through all elements of the matrix and count the negative ones.

2. **Step-by-step**:
   - Initialize `count = 0`
   - For each sublist in the grid:
     - For each number in the sublist:
       - If `num < 0` → increment `count`
   - Return `count`

3. **More efficient alternative approach**: Since the matrix is sorted (non-increasing in rows and columns), we could use a "staircase" approach starting from the top-right corner, reducing the complexity to O(m + n). But for the problem's constraints, the brute force approach is acceptable.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(m × n) — we iterate through the whole matrix |
| **Space** | O(1) — just one counter |
