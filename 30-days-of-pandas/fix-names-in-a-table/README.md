# Fix Names in a Table

| Property | Value |
|-------------|-------|
| **Number** | 1667 |
| **Difficulty** | Easy |
| **Link** | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description) |
| **Language** | Python (Pandas) |

## Description

Fix the names in the table so that only the **first letter** is uppercase and the rest are lowercase. Return sorted by `user_id`.

## Thought Process

1. **Core Idea**: Use the Pandas `.str.capitalize()` method, which transforms the first letter into uppercase and all others into lowercase — exactly what the problem asks for.

2. **Step-by-step**:
   - `users['name'].str.capitalize()` — applies capitalize to each name
   - Assign back: `users['name'] = ...`
   - Sort by `user_id`: `.sort_values(by='user_id')`
   - Return the DataFrame

3. **String methods in Pandas**: The `.str` accessor allows applying Python string methods across an entire Series at once (vectorization). Other examples: `.str.upper()`, `.str.lower()`, `.str.title()`.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n log n) — dominated by sorting |
| **Space** | O(n) — for the modified column |
