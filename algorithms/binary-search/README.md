# Binary Search

| Property | Value |
|-------------|-------|
| **Number** | 704 |
| **Difficulty** | Easy |
| **Link** | [Binary Search](https://leetcode.com/problems/binary-search/description/) |
| **Language** | Python |

## Description

Given a **sorted** (in ascending order) integer array `arr` and an integer `target`, write a function to search `target` in `arr`. If target exists, then return its index. Otherwise, return `-1`.

## Thought Process

1. **Core Idea**: **Binary search** is one of the most fundamental algorithms in computer science. The idea is to eliminate half of the search space in each iteration, taking advantage of the fact that the array is sorted.

2. **Step-by-step**:
   - Create two pointers: `left = 0` and `right = len(arr) - 1`
   - While `left <= right` (there is still space to search):
     - Calculate the middle: `mid = left + (right - left) // 2`
       - We use this formula instead of `(left + right) // 2` to prevent overflow in other languages
     - If `arr[mid] == target` → **found it!** Return `mid`
     - If `arr[mid] < target` → target is in the **right half**: `left = mid + 1`
     - If `arr[mid] > target` → target is in the **left half**: `right = mid - 1`
   - If the loop finishes → target is not in the array → return `-1`

3. **Visual Example**: Array `[1, 3, 5, 7, 9]`, target = 7
   - `left=0, right=4, mid=2` → `arr[2]=5 < 7` → `left=3`
   - `left=3, right=4, mid=3` → `arr[3]=7 == 7` → returns 3 ✓

4. **Why it's efficient**: At each step we eliminate half of the candidates. For an array of 1 million elements, we need at most ~20 comparisons.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(log n) — we divide the space in half at each iteration |
| **Space** | O(1) — only auxiliary variables |
