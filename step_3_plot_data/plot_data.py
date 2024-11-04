import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(grouped_data):
    # Set up the bar chart with platforms on the x-axis and count on the y-axis
    plt.figure(figsize=(12, 6))
    sns.barplot(data=grouped_data, x='platform', y='count', hue='genre')

    # Customize the plot
    plt.xlabel("Platform")
    plt.ylabel("Number of Games")
    plt.title("Number of Games per Genre by Platform")
    plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
