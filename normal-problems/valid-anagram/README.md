# Valid Anagram

| Property | Value |
|-------------|-------|
| **Number** | 242 |
| **Difficulty** | Easy |
| **Link** | [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/) |
| **Languages** | Python, C |

## Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Thought Process

### Python Solution — `Counter`

1. **Core Idea**: Two strings are anagrams if and only if they have **the exact same frequency of each character**. Python's `Counter` automatically creates a frequency dictionary.

2. **Step-by-step**:
   - `Counter(s)` → counts the frequency of each letter in `s`
   - `Counter(t)` → counts the frequency of each letter in `t`
   - Compare them: `Counter(s) == Counter(t)`
   - If they are equal → it's an anagram

### C Solution — Counting Array

1. **Core Idea**: Same logic, but manually implemented with an array of 256 positions (one for each possible ASCII value).

2. **Step-by-step**:
   - First, we check if the lengths are equal (optimization: if not, it's not an anagram)
   - Initialize `count[256] = {0}`
   - For each character: we increment `count[s[i]]` and decrement `count[t[i]]`
   - Finally, if **all** values in `count` are 0, the strings are anagrams
   - Any value different from 0 means one string has more of some character

3. **Why this approach works in C**: Without built-in structures like `Counter`, we use a simple array as a hash map — the index is the ASCII code of the character.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — we iterate through both strings |
| **Space** | O(1) — the counting array has a fixed size (256 or 26) |
