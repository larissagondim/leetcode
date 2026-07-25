# Group Anagrams

| Property       | Value                                                                       |
| -------------- | --------------------------------------------------------------------------- |
| **Number**     | 49                                                                          |
| **Difficulty** | Medium                                                                      |
| **Link**       | [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/) |
| **Language**   | Python                                                                      |

## Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **anagram** is a word formed by rearranging the letters of another word, using the same characters with the same frequencies.

For example:

```text
"eat" -> "tea" -> "ate"
```

All of them contain the same letters, so they belong to the same group.

---

## Thought Process

### 1. Core Idea

The main challenge is identifying which words are anagrams of each other.

The key observation is that two strings are anagrams if, after sorting their characters, they produce the same result.

For example:

```text
"eat" -> "aet"
"tea" -> "aet"
"ate" -> "aet"
```

Since they generate the same key, they can be stored in the same group.

The solution uses a hash map (`dict`) where:

* The **key** is the sorted version of the string;
* The **value** is a list containing all strings with that same key.

---

### 2. Step-by-step

The solution follows this flow:

* Create an empty dictionary to store the groups;
* Iterate through each string in `strs`;
* Sort the characters of the current string to create a unique key;
* Check if this key already exists in the dictionary;
* If it does not exist, create a new empty list;
* Add the original string to the corresponding group;
* Return all dictionary values as a list.

---

### 3. Example with simulation

```text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

grupos = {}
```

Processing each string:

| Current string | Sorted key | Action                        |
| -------------- | ---------- | ----------------------------- |
| `"eat"`        | `"aet"`    | Create group and add `"eat"`  |
| `"tea"`        | `"aet"`    | Add `"tea"` to existing group |
| `"tan"`        | `"ant"`    | Create group and add `"tan"`  |
| `"ate"`        | `"aet"`    | Add `"ate"` to existing group |
| `"nat"`        | `"ant"`    | Add `"nat"` to existing group |
| `"bat"`        | `"abt"`    | Create group and add `"bat"`  |

Final dictionary:

```text
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

Returned result:

```text
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

### 4. Concept

This problem focuses on **hash maps** and **string normalization**.

The important idea is transforming different representations of the same data into a common format.

By sorting each word, all anagrams receive the same identifier, making it efficient to group them together using a dictionary.

---

## Complexity

| Type      | Complexity                                                                                               |
| --------- | -------------------------------------------------------------------------------------------------------- |
| **Time**  | O(n * k log k) — where `n` is the number of strings and `k` is the length of each string, due to sorting |
| **Space** | O(n * k) — stores all strings inside the hash map                                                        |
|           |                                                                                                          |
