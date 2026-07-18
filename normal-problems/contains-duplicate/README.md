# Contains Duplicate

| Property | Value |
|-------------|-------|
| **Number** | 217 |
| **Difficulty** | Easy |
| **Link** | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/) |
| **Language** | Python |

## Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Thought Process

1. **Core Idea**: A **set** in Python stores only unique values. If we convert the array into a set and the size is different from the original, there are duplicates.

2. **Step-by-step**:
   - Create a set from the array: `unique = set(nums)`
   - Compare the lengths: `len(unique) != len(nums)`
   - If they are different → there are duplicates → return `True`
   - If they are equal → all are unique → return `False`

3. **Why it's elegant**: This approach solves the problem in a single line, taking advantage of the set's natural property of eliminating duplicates.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — set construction |
| **Space** | O(n) — set storage |
