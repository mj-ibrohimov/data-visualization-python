## Step 1: Loading and Inspecting the Dataset

### Objective:
In this step, you'll learn how to load a dataset using the Pandas library and filter it to include only specific platforms (PS4, XOne, PC, and WiiU).

### Theory:
- **Loading Data**: Pandas provides a simple way to load data from CSV files using the `pd.read_csv()` function.
- **Filtering Data**: Once the data is loaded, you can filter rows using conditional expressions.

### Instructions:
1. Load the dataset using Pandas.
2. Filter the dataset to include only rows where the `platform` column is one of the following: PS4, XOne, PC, or WiiU.
3. Print the first few rows of the filtered data to inspect.

### Expected Output:
After completing this step, you should have a filtered DataFrame with only the required platforms. The first few rows should look something like this:

| name                    | platform | year_of_release | genre       | ... |
|-------------------------|----------|-----------------|-------------|-----|
| Call of Duty: Black Ops 3 | PS4      | 2015            | Shooter     | ... |
| Grand Theft Auto V      | PS4      | 2014            | Action      | ... |

