import unittest
import sys
import os
import pandas as pd

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from step_2_prepare_data.prepare_data import prepare_data
from step_1_load_data.load_data import load_and_filter_data
from plot_data import plot_data

class TestPlotData(unittest.TestCase):
    
    def test_plot_data(self):
        # Load and prepare sample data (replace with the path to `games_data.csv`)
        file_path = 'data/games_data.csv'
        data = load_and_filter_data(file_path)
        grouped_data = prepare_data(data)
        
        # Run the plot function to ensure no errors occur
        try:
            plot_data(grouped_data)
            result = True
        except Exception as e:
            print(f"Error in plotting function: {e}")
            result = False
            
        self.assertTrue(result, "Plotting function raised an error.")
        
if __name__ == '__main__':
    unittest.main()
