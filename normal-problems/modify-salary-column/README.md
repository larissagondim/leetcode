# Modify Salary Column

| Property | Value |
|-------------|-------|
| **Difficulty** | Easy |
| **Link** | [LeetCode](https://leetcode.com/) |
| **Language** | Python (Pandas) |

## Description

Given a DataFrame `employees` with columns `name` and `salary`, modify the `salary` column by multiplying all values by 2.

## Thought Process

1. **Core Idea**: Use Pandas **vectorized operation**. Instead of iterating row by row, we apply the multiplication directly to the entire column.

2. **Step-by-step**:
   - `employees['salary'] *= 2` — multiplies all salaries by 2 at once
   - Return the modified DataFrame

3. **Why vectorization**: Vectorized operations in Pandas are significantly faster than `for` loops because they use optimized C operations under the hood (NumPy).

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — vectorized operation over n rows |
| **Space** | O(1) — in-place modification |
