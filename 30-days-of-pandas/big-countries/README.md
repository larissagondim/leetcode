# Big Countries

| Property | Value |
|-------------|-------|
| **Number** | 595 |
| **Difficulty** | Easy |
| **Link** | [Big Countries](https://leetcode.com/problems/big-countries/description/) |
| **Language** | Python (Pandas) |

## Description

A country is considered "big" if it has an **area** of at least 3 million km² **or** a **population** of at least 25 million. Return the name, population, and area of the big countries.

## Thought Process

1. **Core Idea**: Filtering with a compound condition using the Pandas `|` (logical OR) operator.

2. **Step-by-step**:
   - Create the condition: `(world['area'] >= 3000000) | (world['population'] >= 25000000)`
   - Use `.loc[condition, ['name', 'population', 'area']]` to select only the desired columns of the countries that satisfy the condition

3. **Important Detail**: In Pandas, we use `|` instead of `or` for element-wise operations in Series. Each sub-condition must be enclosed in parentheses for correct operator precedence.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — iterates through all rows |
| **Space** | O(k) — where k = number of big countries |
