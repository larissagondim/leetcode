# Search Insert Position

| Property | Value |
|-------------|-------|
| **Number** | 35 |
| **Difficulty** | Easy |
| **Link** | [Search Insert Position](https://leetcode.com/problems/search-insert-position/description/) |
| **Language** | Python |

## Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## Thought Process

1. **Core Idea**: Apply **binary search**. The array is already sorted, so we can eliminate half of the candidates at each iteration.

2. **Step-by-step**:
   - Define `left = 0` and `right = len(nums) - 1`
   - While `left <= right`:
     - Calculate `mid = left + (right - left) // 2` (prevents overflow)
     - If `nums[mid] == target` → found it, return `mid`
     - If `nums[mid] < target` → target is to the right, `left = mid + 1`
     - If `nums[mid] > target` → target is to the left, `right = mid - 1`
   - If the loop ends without finding: `left` is exactly the insertion position

3. **Why `left` is the insertion position**: When the loop ends, `left > right`. At this point, `left` points to the first element greater than `target` — exactly where `target` should be inserted to maintain order.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(log n) — binary search |
| **Space** | O(1) — only auxiliary variables |
