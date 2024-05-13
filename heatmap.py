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
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()

    # Group correlations by strength of relationship
    strong_correlations = []
    moderate_correlations = []
    weak_correlations = []
    for col1 in corr.columns:
        for col2 in corr.columns:
            if col1 != col2:
                correlation = corr.loc[col1, col2]
                if abs(correlation) >= 0.5:  # Strong correlation threshold
                    strong_correlations.append((col1, col2, correlation))
                elif abs(correlation) >= 0.3:  # Moderate correlation threshold
                    moderate_correlations.append((col1, col2, correlation))
                else:
                    weak_correlations.append((col1, col2, correlation))
    # Print summary
    print("Summary of Correlation Analysis:")
    print("Strong Relationships:")
    for correlation in strong_correlations:
        print(f"The correlation between {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}")
    print("\nModerate Relationships:")
    for correlation in moderate_correlations:
        print(f"The correlation between {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}")
    print("\nWeak Relationships:")
    for correlation in weak_correlations:
        print(f"The correlation between {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}")

if __name__ == "__main__":
    create_heatmap('iris.data')