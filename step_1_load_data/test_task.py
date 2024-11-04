import unittest
import pandas as pd
from load_data import load_and_filter_data

class TestLoadData(unittest.TestCase):
    
    def test_load_and_filter_data(self):
        # Load a sample dataset (replace with file path to `games_data.csv`)
        file_path = 'data/games_data.csv'
        
        # Load and filter data
        data = load_and_filter_data(file_path)
        
        # Check if only the specified platforms are present
        platforms = ["PS4", "XOne", "PC", "WiiU"]
        self.assertTrue(all(data['platform'].isin(platforms)))
        
        # Check if the dataset is not empty
        self.assertGreater(len(data), 0)
        
if __name__ == '__main__':
    unittest.main()
