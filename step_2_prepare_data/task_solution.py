import pandas as pd

def prepare_data(data):
    # Group by platform and genre and count the number of games in each group
    grouped_data = data.groupby(['platform', 'genre']).size().reset_index(name='count')
    return grouped_data
