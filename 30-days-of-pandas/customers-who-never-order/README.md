# Customers Who Never Order

| Property | Value |
|-------------|-------|
| **Number** | 183 |
| **Difficulty** | Easy |
| **Link** | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/description/) |
| **Language** | Python (Pandas) |

## Description

Given the `Customers` and `Orders` tables, find all customers who **never** placed an order.

## Thought Process

1. **Core Idea**: We need to find customer IDs that **do not appear** in the orders table. This is equivalent to an **anti-join** operation — finding elements in A that are not in B.

2. **Step-by-step**:
   - `~customers['id'].isin(orders['customerId'])` — creates a boolean mask: `True` for customers whose ID is **not** in the `customerId` column of `orders`
   - `customers.loc[condition, ['name']]` — filters only the names of the customers who satisfy the condition
   - `.rename(columns={'name': 'Customers'})` — renames the column as expected by the output

3. **Key Operators**:
   - `isin()` — checks membership in a set of values
   - `~` — NOT operator, inverts the boolean mask
   - `.loc[]` — label/condition-based selection

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n + m) — where n = customers, m = orders |
| **Space** | O(m) — for the set of order IDs |
