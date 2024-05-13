# Program: heatmap.py
# This program: 4. Outputs a heatmap with the correlation between the pair of variables
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

    # Group correlations by strength of relationship
    strong_correlations = []
    moderate_correlations = []
    weak_correlations = []
    for col1 in corr.columns:
        for col2 in corr.columns:
            if col1 < col2:  # Filter out mirrored correlations
                correlation = corr.loc[col1, col2]
                if abs(correlation) >= 0.5:  # Strong correlation threshold
                    strong_correlations.append((col1, col2, correlation))
                elif abs(correlation) >= 0.3:  # Moderate correlation threshold
                    moderate_correlations.append((col1, col2, correlation))
                else:
                    weak_correlations.append((col1, col2, correlation))

    # Sort correlations within each category based on correlation value
    strong_correlations.sort(key=lambda x: x[2], reverse=True)
    moderate_correlations.sort(key=lambda x: x[2], reverse=True)
    weak_correlations.sort(key=lambda x: x[2], reverse=True)

    # Print summary
    print("5. Summary of Correlation Analysis:\n")
    print("For x = correlation coefficient between each two variables of the Iris dataset, the following assumptions can be made: \n")
    print("Strong Relationships 'abs(x)>= 0.5':")
    for correlation in strong_correlations:
        print(f" - {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}")
    print("\nModerate Relationships 'abs(x)>= 0.3':")
    for correlation in moderate_correlations:
        print(f" - {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}")
    print("\nWeak Relationships 'abs(x) < 0.3':")
    for correlation in weak_correlations:
        print(f" - {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}")

if __name__ == "__main__":
    create_heatmap('iris.data')