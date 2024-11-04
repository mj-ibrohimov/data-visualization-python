# Data Visualization Project

## Overview
This project is a data visualization tool designed to load, filter, and analyze data on various gaming platforms and genres. Using Python, Pandas, Seaborn, and Matplotlib, this project reads a CSV dataset, processes it, and creates insightful visualizations of the data.

## Project Structure
The project is organized into three primary folders, each focusing on a specific task within the project pipeline:

1. **Step 1: Data Loading and Filtering**  
   - **File:** `step_1_load_data/load_data.py`
   - **Function:** `load_and_filter_data(file_path)`
   - **Description:** Loads the dataset from a specified CSV file, filters for select platforms (`PS4`, `XOne`, `PC`, and `WiiU`), and returns the filtered dataset.

2. **Step 2: Data Preparation**  
   - **File:** `step_2_prepare_data/prepare_data.py`
   - **Function:** `prepare_data(data)`
   - **Description:** Groups the data by platform and genre, counts the number of games per combination, and returns the grouped dataset for further analysis and plotting.

3. **Step 3: Data Visualization**  
   - **File:** `plot_data/plot_data.py`
   - **Function:** `plot_data(grouped_data)`
   - **Description:** Generates a bar chart showing the number of games per genre by platform using Seaborn and Matplotlib. The chart includes a legend for genres and presents platforms on the x-axis and game counts on the y-axis.

## Installation

### Prerequisites
- Python 3.6+
- `pip` package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/mj-ibrohimov/data-visualization-python.git
   cd data-visualization-python

## Install required packages:
```bash
pip install -r requirements.txt
```

# Usage
**Run Tests**
Tests for each module are included to ensure functionality. Use the following command to run all tests:

```bash
python -m unittest discover -s tests
```
Run the Pipeline After ensuring the dataset (e.g., games_data.csv) is in the data folder, run the modules sequentially:

Load and filter data:

```python
from step_1_load_data.load_data import load_and_filter_data
data = load_and_filter_data('data/games_data.csv')
```
Prepare data:

```python
from step_2_prepare_data.prepare_data import prepare_data
grouped_data = prepare_data(data)
```
Plot data:

```python
from plot_data.plot_data import plot_data
plot_data(grouped_data)
```
### File Details
requirements.txt
Lists the Python packages required to run this project, including pandas, seaborn, and matplotlib.

data/games_data.csv
The CSV file containing data on various gaming platforms and genres. Ensure this file exists in the data folder.

Tests Folder
Contains unit tests for each function, verifying the functionality of data loading, preparation, and visualization modules.

## Example Output
The bar chart generated in Step 3 displays each platform on the x-axis, with bars representing the number of games for each genre. This visualization provides a comparative view of genre distribution across platforms.
