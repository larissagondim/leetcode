# Valid Parentheses

| Property | Value |
|-------------|-------|
| **Number** | 20 |
| **Difficulty** | Easy |
| **Link** | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/) |
| **Language** | Python |

## Description

Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[` and `]`, determine if the input string is valid. An input string is valid if open brackets must be closed by the same type of brackets, and in the correct order.

## Thought Process

1. **Core Idea**: Use a **stack** — LIFO structure (Last In, First Out). Whenever we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the top of the stack has the corresponding matching pair.

2. **Step-by-step**:
   - Iterate through each character of the string
   - If it's an **opening** bracket (`(`, `{`, `[`): push onto the stack
   - If it's a **closing** bracket (`)`, `}`, `]`):
     - If the stack is empty → invalid (no matching open bracket)
     - If the top of the stack is the matching pair → pop from stack
     - Otherwise → invalid (mismatched pair)
   - At the end, the string is valid **if and only if** the stack is empty

3. **Why a stack is perfect here**: Brackets must be closed in the reverse order in which they were opened — exactly the LIFO behavior of a stack. Ex: `([{}])` — the `{` is the last one to open and the first one to close.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — we traverse the string once |
| **Space** | O(n) — in the worst case, all characters are opening brackets |
