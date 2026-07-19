# Remove Element

| Property       | Value                                                                       |
| -------------- | --------------------------------------------------------------------------- |
| **Number**     | 27                                                                          |
| **Difficulty** | Easy                                                                        |
| **Link**       | [Remove Element](https://leetcode.com/problems/remove-element/description/) |
| **Language**   | Python                                                                      |

## Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

## Thought Process

### 1. Core Idea

To remove all occurrences of a specific number, my first idea was the following:

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)  # k starts as the size of the list

        while val in nums:  # keeps searching for val
            nums.remove(val)  # removes the first occurrence
            k -= 1

        return k
```

Did it work? **Yes.**

Was it the most efficient? **Definitely not.**

Although this solution was accepted, both `val in nums` and `remove()` require traversing the list. Since this process is repeated for every occurrence of `val`, the overall complexity can become **O(n²)**.

Instead of removing elements one by one, I changed my perspective and started thinking about **keeping** the elements I wanted.

This naturally led me to the **Two Pointers** technique.

---

### 2. Step-by-step

The idea is to use a pointer `k` that always represents the **next position where a valid element should be placed**.

For every element in `nums`:

* If it is **different** from `val`,

  * copy it to position `k`;
  * increment `k`.
* Otherwise, ignore it.

At the end, the first `k` positions of the array contain exactly the elements we want to keep.

---

### 3. Example with simulation

```text
nums = [1, 2, 2, 3, 4]
val = 2
```

| Current number | Action          | Array           | k |
| -------------- | --------------- | --------------- | - |
| 1              | Keep            | [1, 2, 2, 3, 4] | 1 |
| 2              | Skip            | [1, 2, 2, 3, 4] | 1 |
| 2              | Skip            | [1, 2, 2, 3, 4] | 1 |
| 3              | Copy to index 1 | [1, 3, 2, 3, 4] | 2 |
| 4              | Copy to index 2 | [1, 3, 4, 3, 4] | 3 |

The first `k` elements are now:

```text
[1, 3, 4]
```

The remaining values in the array don't matter because the problem only evaluates the first `k` positions.

---

### 4. Concept

This problem is a classic application of the **Two Pointers** technique.

Instead of repeatedly removing elements—which causes the remaining elements to shift—we simply overwrite the beginning of the array with the values we want to keep.

This allows us to solve the problem in a **single pass**, using constant extra space.

## Complexity

| Type      | Complexity                        |
| --------- | --------------------------------- |
| **Time**  | O(n) — one pass through the array |
| **Space** | O(1) — in-place modification      |
