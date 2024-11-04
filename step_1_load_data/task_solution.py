import pandas as pd

def load_and_filter_data(file_path):
    data = pd.read_csv(file_path)
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_data = data[data['platform'].isin(platforms)]
    return filtered_data
