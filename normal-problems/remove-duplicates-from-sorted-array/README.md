# Remove Duplicates from Sorted Array

| Property | Value |
|-------------|-------|
| **Number** | 26 |
| **Difficulty** | Easy |
| **Link** | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/) |
| **Language** | Python |

## Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

## Thought Process

1. **Core Idea**: Use the **two pointers** technique. Since the array is already sorted, duplicates will always be adjacent. We use a pointer `k` to mark the position where the next unique element should be placed.

2. **Step-by-step**:
   - Initialize `k = 1` (the first element is always unique)
   - Iterate starting from index 1
   - If `nums[i-1] != nums[i]` → we found a new unique value:
     - Place it at position `k`
     - Increment `k`
   - If they are equal → just move forward, ignoring the duplicate

3. **Visual Example**: `[1, 1, 2, 3, 3]`
   - `i=1`: `1 == 1` → skip
   - `i=2`: `1 != 2` → `nums[1] = 2`, `k=2`
   - `i=3`: `2 != 3` → `nums[2] = 3`, `k=3`
   - `i=4`: `3 == 3` → skip
   - Result: `[1, 2, 3, ...]`, `k=3`

4. **Why it works in-place**: We don't create a new array. We just reorganize the existing elements, using `k` as a writing cursor.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — a single pass through the array |
| **Space** | O(1) — in-place modification |
