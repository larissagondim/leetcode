# Two Sum

| Property | Value |
|-------------|-------|
| **Number** | 1 |
| **Difficulty** | Easy |
| **Link** | [Two Sum](https://leetcode.com/problems/two-sum/description/) |
| **Language** | Python |

## Description

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

## Thought Process

1. **Core Idea**: For each number in the array, the "complement" we need to find is `target - nums[i]`. If this complement exists in the array (at a different position), we found the pair.

2. **Using a hash map (dictionary)**: Instead of using two nested loops (O(n²)), we create a dictionary that maps each **value** to its **index** — `{value: index}`. This allows us to search for the complement in O(1) time.

3. **Step-by-step**:
   - Build the dictionary: `dict = {nums[i]: i for i in range(len(nums))}`
   - For each element `nums[i]`, calculate `complement = target - nums[i]`
   - Check if `complement` is in the dictionary **and** if it's not the same index (so we don't use the same element twice)
   - If found, return `[dict[complement], i]`

4. **Why it works**: The dictionary guarantees O(1) lookup for the complement, transforming the problem from O(n²) to O(n).

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) |
| **Space** | O(n) — for the auxiliary dictionary |
