## Step 2: Preparing Data for Plotting

### Objective:
In this step, you'll learn how to group data by platform and genre, and count the number of games in each group. This information will allow us to create a bar chart showing the distribution of game genres across the selected platforms.

### Theory:
- **Grouping and Counting**: Pandas provides the `groupby()` function to organize data by specified columns, and `size()` or `count()` can be used to count rows in each group.
- **Data Transformation**: After grouping, ensure the data is in a format where each platform and genre has an associated count value, ready for visualization.

### Instructions:
1. Use the filtered data from Step 1 as input.
2. Group the data by `platform` and `genre`, then count the number of games in each group.
3. Return a DataFrame with columns `platform`, `genre`, and `count` (indicating the number of games).

### Expected Output:
After completing this step, you should have a DataFrame that looks something like this:

| platform | genre       | count |
|----------|-------------|-------|
| PS4      | Action      | 140   |
| PS4      | Sports      | 80    |
| XOne     | Shooter     | 60    |
| PC       | Puzzle      | 20    |
| WiiU     | Racing      | 10    |

This format will be suitable for plotting a bar chart in the next step.
