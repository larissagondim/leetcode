# Length of Last Word

| Property       | Value                                                                                 |
| -------------- | ------------------------------------------------------------------------------------- |
| **Number**     | 58                                                                                    |
| **Difficulty** | Easy                                                                                  |
| **Link**       | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/) |
| **Language**   | Python                                                                                |

## Description

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A word is a maximal substring consisting of non-space characters only.

---

## Thought Process

### 1. Core Idea

The main goal is to find the last word in the string and count its characters.

Instead of scanning the entire string from the beginning, the idea is to start from the end, where the target word is located. By traversing the string backwards, we can ignore trailing spaces and count characters until reaching the beginning of the word.

---

### 2. Step-by-step

The solution follows a simple flow:

* Traverse the string from the end to the beginning;
* Ignore spaces at the end of the string;
* Count every non-space character;
* Stop counting when a space is found after the word has started;
* Return the counter value.

---

### 3. Example with simulation

```text
s = "  bye bye "
size = 0
```

Starting from the end of the string:

| Current char | Action                 | `size` value |
| ------------ | ---------------------- | ------------ |
| `' '`        | Ignore trailing spaces | 0            |
| `'e'`        | Increment              | 1            |
| `'y'`        | Increment              | 2            |
| `'b'`        | Increment              | 3            |
| `' '`        | Stop iteration         | 3            |

The length of the last word (`"bye"`) is **3**.

---

### 4. Concept

This problem focuses on string traversal and identifying substrings based on conditions.

The key observation is that the last word is always found near the end of the string, so traversing backwards avoids unnecessary work.

---

## Complexity

| Type      | Complexity                                              |
| --------- | ------------------------------------------------------- |
| **Time**  | O(n) — in the worst case, the whole string is traversed |
| **Space** | O(1) — only a counter and indexes are used              |
