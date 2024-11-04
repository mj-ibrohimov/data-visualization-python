import pandas as pd

def load_and_filter_data(file_path):
    # Load the dataset from the given file path
    data = pd.read_csv(file_path)
    
    # Filter data to include only specified platforms
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_data = data[data['platform'].isin(platforms)]
    
    # Display the first few rows of the filtered data
    print(filtered_data.head())
    
    return filtered_data
