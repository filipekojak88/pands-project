# Program: heatmap.py
# This program outputs a heat map with the correlation of each pair of variables
# Author: Filipe Carvalho


# Import necessary libraries

# Import the load_dataset function from custom load_iris.py
from load_iris import load_dataset
# Import matplotlib for plotting and setting the size of the figure and the title of the heatmap plot
import matplotlib.pyplot as plt
# Import seaborn for advanced data visualization
import seaborn as sns

def create_heatmap(file_name):
    """
    Creates a correlation heatmap for the given dataset file.

    Parameter:
        file_name: Name of the file containing the Iris DataSet.
    """
    # Load the dataset
    df = load_dataset(file_name)

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Calculate correlation matrix
    corr = numeric_df.corr()
    

    # Create a heatmap plot

    # Set the figure size
    plt.figure(figsize=(10, 8))
    # Create the heatmap with Seaborn
    ax = sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    # Set the title of the heatmap plot
    plt.title('Correlation Heatmap')
    
    # Define legend labels for different strength levels of relationships
    legend_labels = {
    'Strong Relationships (|x| ≥ 0.5)': 0.5,
    'Moderate Relationships (0.3 ≤ |x| < 0.5)': 0.4,
    'Weak Relationships (|x| < 0.3)': 0.2
    }


    # Add legend annotations to the bottom of the chart, side by side

    # Initialize an empty list to hold legend handles
    handles = []
    # Iterate over legend labels and thresholds
    for label, threshold in legend_labels.items():
        # Create dummy scatterplots for each label
        handles.append(ax.scatter([], [], color='black', label=label))
    # Add legend with specified properties
    plt.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=10)
    
    # Display the heatmap
    plt.show()

# If this script is executed as the main program
if __name__ == "__main__":
    # Execute create_heatmap using the 'iris.data' dataset as an argument 
    create_heatmap('iris.data')