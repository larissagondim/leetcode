# Article Views I

| Property | Value |
|-------------|-------|
| **Number** | 1148 |
| **Difficulty** | Easy |
| **Link** | [Article Views I](https://leetcode.com/problems/article-views-i/description/) |
| **Language** | Python (Pandas) |

## Description

Find all the authors that viewed at least one of their own articles. Return the IDs sorted in ascending order.

## Thought Process

1. **Core Idea**: An author viewed their own article when `author_id == viewer_id` in the same row. We need to collect these IDs **uniquely** and **sorted**.

2. **Step-by-step**:
   - We initialize an empty list `ids`
   - Iterate through each row of the DataFrame:
     - If `author_id == viewer_id` **and** the ID is not yet in the list → we add it
   - Sort the list: `ids.sort()`
   - Return as DataFrame: `pd.DataFrame({"id": ids})`

3. **Alternative idiomatic approach**:
   ```python
   df = views[views['author_id'] == views['viewer_id']][['author_id']].drop_duplicates()
   return df.rename(columns={'author_id': 'id'}).sort_values('id')
   ```
   This would be more efficient and "Pandas-like", avoiding the explicit loop.

## Complexity

| Type | Complexity |
|------|-------------|
| **Time** | O(n²) — due to the `not in ids` inside the loop (list) |
| **Space** | O(k) — where k = number of unique authors who viewed their own articles |
