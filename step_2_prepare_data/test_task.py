import unittest
import pandas as pd
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can use absolute imports
from step_2_prepare_data.prepare_data import prepare_data
from step_1_load_data.load_data import load_and_filter_data

class TestPrepareData(unittest.TestCase):
    
    def test_prepare_data(self):
        # Load a sample dataset and filter it (replace with the file path to `games_data.csv`)
        file_path = 'data/games_data.csv'
        data = load_and_filter_data(file_path)
        
        # Prepare data for plotting
        grouped_data = prepare_data(data)
        
        # Check if grouped_data has the expected columns
        self.assertListEqual(list(grouped_data.columns), ['platform', 'genre', 'count'])
        
        # Check if count column is integer type
        self.assertTrue(pd.api.types.is_integer_dtype(grouped_data['count']))
        
        # Check if the grouped_data is not empty
        self.assertGreater(len(grouped_data), 0)
        
if __name__ == '__main__':
    unittest.main()
