# Program: correlation.py
# This program: 5. Outputs a correlation analysis of each variable,
# and append to the single text file created in summary.py
# Author: Filipe Carvalho


# Import necessary libraries

# Import the load_dataset function from load_iris.py
from load_iris import load_dataset

def create_correlation(file_name):
    # Load the dataset
    df = load_dataset(file_name)

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Calculate correlation matrix
    corr = numeric_df.corr()

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

    # Build correlation analysis as a string
    correlation_output = ""
    correlation_output += "For x = correlation coefficient between each two variables of the Iris dataset, the following assumptions can be made: \n\n"
    correlation_output += "Strong Relationships 'abs(x)>= 0.5':\n"
    for correlation in strong_correlations:
        correlation_output += f"- {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}\n"
    correlation_output += "\nModerate Relationships 'abs(x)>= 0.3':\n"
    for correlation in moderate_correlations:
        correlation_output += f"- {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}\n"
    correlation_output += "\nWeak Relationships 'abs(x) < 0.3':\n"
    for correlation in weak_correlations:
        correlation_output += f"- {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}\n"

    # Return the correlation analysis as a string
    return correlation_output

if __name__ == "__main__":
    # Modify the call to create_correlation to assign its output to a variable
    correlation_result = create_correlation('iris.data')
    # Print the result
    print(correlation_result)
