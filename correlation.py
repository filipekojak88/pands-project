# Program: correlation.py
# This program outputs a correlation analysis of each pair of variable,
# Author: Filipe Carvalho


# Import necessary libraries

# Import the load_dataset function from load_iris.py
from load_iris import load_dataset

def create_correlation(file_name):
    """
    Creates a correlation analysis summary for the given dataset file.

    Parameter:
        file_name: Name of the file containing the Iris DataSet.
    """
    # Load the dataset
    df = load_dataset(file_name)

    # Select only numeric columns for correlation analysis
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Calculate correlation matrix
    corr = numeric_df.corr()

    # Group correlations by strength of relationship
    
    # Holds correlations with |correlation coefficient| ≥ 0.5
    strong_correlations = []
    # Holds correlations with 0.3 ≤ |correlation coefficient| < 0.5
    moderate_correlations = []
    # Holds correlations with |correlation coefficient| < 0.3
    weak_correlations = []

    # Iterate over each pair of columns to calculate correlations
    for col1 in corr.columns:
        # Iterate over the remaining columns to avoid redundant calculations
        for col2 in corr.columns:
            # Filter out mirrored correlations and only consider unique pairs
            if col1 < col2: 
                # Calculate the correlation coefficient between the two columns 
                correlation = corr.loc[col1, col2]
                # Check if the correlation coefficient indicates a strong relationship
                if abs(correlation) >= 0.5:  
                    # Store the pair of columns and their correlation coefficient in the strong_correlations list
                    strong_correlations.append((col1, col2, correlation))
                # Check if the correlation coefficient indicates a moderate relationship
                elif abs(correlation) >= 0.3:  
                    # Store the pair of columns and their correlation coefficient in the moderate_correlations list
                    moderate_correlations.append((col1, col2, correlation))
                # If the correlation coefficient does not meet the thresholds for strong or moderate correlation 
                else:
                    # Store the pair of columns and their correlation coefficient in the weak_correlations list
                    weak_correlations.append((col1, col2, correlation))


    # Sort correlations within each category based on the absolute value of correlation coefficient
    
    # Sort strong correlations in descending order of correlation coefficient
    strong_correlations.sort(key=lambda x: x[2], reverse=True)
    # Sort moderate correlations in descending order of correlation coefficient
    moderate_correlations.sort(key=lambda x: x[2], reverse=True)
    # Sort weak correlations in descending order of correlation coefficient
    weak_correlations.sort(key=lambda x: x[2], reverse=True)


    # Build correlation analysis as a string
    correlation_output = ""
    # Add header describing the correlation analysis
    correlation_output += "For x = correlation coefficient between each two variables of the Iris dataset, the following assumptions can be made: \n\n"
    
    # Add section for strong relationships (|correlation coefficient| ≥ 0.5)
    correlation_output += "Strong Relationships 'abs(x)>= 0.5':\n"
    # Iterate over strong correlations and add them to the summary
    for correlation in strong_correlations:
        # Add formatted string to include column names and their corresponding correlation coefficient in the summary
        correlation_output += f"- {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}\n"

    # Add section for moderate relationships (0.3 ≤ |correlation coefficient| < 0.5)
    correlation_output += "\nModerate Relationships 'abs(x)>= 0.3':\n"
    # Iterate over moderate correlations and add them to the summary
    for correlation in moderate_correlations:
        # Add formatted string to include column names and their corresponding correlation coefficient in the summary
        correlation_output += f"- {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}\n"

    # Add section for weak relationships (|correlation coefficient| < 0.3)
    correlation_output += "\nWeak Relationships 'abs(x) < 0.3':\n"
    # Iterate over weak correlations and add them to the summary
    for correlation in weak_correlations:
        # Add formatted string to include column names and their corresponding correlation coefficient in the summary
        correlation_output += f"- {correlation[0]} and {correlation[1]} is {correlation[2]:.2f}\n"

    # Return a string containing the correlation analysis summary
    return correlation_output

# If this script is executed as the main program
if __name__ == "__main__":
    # Execute create_correlation using the 'iris.data' dataset as an argument 
    create_correlation('iris.data')
   
