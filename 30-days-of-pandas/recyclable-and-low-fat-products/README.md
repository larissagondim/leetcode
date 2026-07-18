# Recyclable and Low Fat Products

| Property | Value |
|-------------|-------|
| **Number** | 1757 |
| **Difficulty** | Easy |
| **Link** | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/description/) |
| **Language** | Python (Pandas) |

## Description

Find the IDs of the products that are **both** recyclable (`recyclable = 'Y'`) and low fat (`low_fats = 'Y'`).

## Thought Process

1. **Core Idea**: Filtering with a compound condition using the Pandas `&` (logical AND) operator.

2. **Step-by-step**:
   - Condition 1: `products['recyclable'] == 'Y'`
   - Condition 2: `products['low_fats'] == 'Y'`
   - Combine with AND: `(condition1) & (condition2)`
   - Select only the `product_id` column: `.loc[condition, ['product_id']]`

3. **Syntax Detail**: Each sub-condition must be enclosed in **parentheses** because of the precedence of the `&` operator in Python — without parentheses, the comparison operator `==` would have different precedence and cause an error.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — iterates through all rows |
| **Space** | O(k) — where k = products satisfying both conditions |
