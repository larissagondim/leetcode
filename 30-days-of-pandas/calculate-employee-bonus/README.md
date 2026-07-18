# Calculate Employee Bonus

| Property | Value |
|-------------|-------|
| **Number** | 1873 |
| **Difficulty** | Easy |
| **Link** | [Calculate Employee Bonus](https://leetcode.com/problems/calculate-employee-bonus/) |
| **Language** | Python (Pandas) |

## Description

Calculate the bonus of each employee. An employee gets a bonus equal to their salary if: the `employee_id` is **odd** and the name **does not start with 'M'**. Otherwise, the bonus is 0. Return ordered by `employee_id`.

## Thought Process

1. **Core Idea**: Create a bonus column initialized to 0 and then fill in the values for the employees who satisfy the conditions.

2. **Step-by-step**:
   - Build the compound condition:
     - `~employees['name'].str.startswith('M')` — name does NOT start with 'M'
     - `employees['employee_id'] % 2 != 0` — ID is odd
     - Combine with `&`
   - Initialize the bonus column with 0: `employees['bonus'] = 0`
   - For those who satisfy the condition, assign the salary as a bonus:
     `employees.loc[condition, 'bonus'] = employees.loc[condition, 'salary']`
   - Select the required columns and sort: `[['employee_id', 'bonus']].sort_values('employee_id')`

3. **Masking Technique**: We use `.loc` with a boolean mask for both reading and writing. This allows assigning values selectively, without loops.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n log n) — dominated by sorting |
| **Space** | O(n) — for the new bonus column |
