# Program: heatmap.py
# This program: 4. Outputs a heatmap with the correlation of each pair of variables
# Author: Filipe Carvalho


# Import necessary libraries

# Import the load_dataset function from load_iris.py
from load_iris import load_dataset

import matplotlib.pyplot as plt

import seaborn as sns

def create_heatmap(file_name):
    # Load the dataset
    df = load_dataset(file_name)

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Calculate correlation matrix
    corr = numeric_df.corr()
    
    # Create a heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap')
    
    legend_labels = {
    'Strong Relationships (|x| ≥ 0.5)': 0.5,
    'Moderate Relationships (0.3 ≤ |x| < 0.5)': 0.4,
    'Weak Relationships (|x| < 0.3)': 0.2
    }

    # Add legend annotations to the bottom of the chart, side by side
    handles = []
    for label, threshold in legend_labels.items():
        handles.append(ax.scatter([], [], color='black', label=label))
    plt.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=10)

    plt.show()

    
if __name__ == "__main__":
    create_heatmap('iris.data')