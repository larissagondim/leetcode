# Invalid Tweets

| Property | Value |
|-------------|-------|
| **Number** | 1683 |
| **Difficulty** | Easy |
| **Link** | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/description/) |
| **Language** | Python (Pandas) |

## Description

Find the IDs of the invalid tweets — a tweet is invalid if the number of characters in the content is **strictly greater than 15**.

## Thought Process

### Implemented Solution — explicit loop

1. **Step-by-step**:
   - Initialize a list `invalid`
   - Iterate through each tweet:
     - If `len(content) > 15` → add the `tweet_id` to the list
   - Return as DataFrame

### Alternative Solution (commented in code) — idiomatic

```python
tweets.loc[tweets['content'].str.len() > 15, ['tweet_id']]
```

1. **Idea**: Use `.str.len()` to calculate the length of each tweet in a vectorized way, then filter with `.loc[]`

2. **Why the alternative is better**: Avoids explicit loop, is more readable, and leverages Pandas vectorization for better performance.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n) — iterates through all tweets |
| **Space** | O(k) — where k = number of invalid tweets |
