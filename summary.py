# Program: summary.py
# This program: 
# 1. Outputs a summary of each variable to a single text file.
# 2. Provides an overview of the first 5 rows and last 5 rows of the dataset.
# Author: Filipe Carvalho

# Import necessary libraries
import pandas as pd  # For data summary
import io  # To use a string buffer for df.info()
from load_iris import load_dataset  # To load the iris dataset 
from correlation import create_correlation  # To do the correlation analysis

def create_summary(file_name):
    """
    Generates a summary of each variable in the dataset, provides an overview of the first 5 rows
    and last 5 rows of the dataset, and saves it all to a text file.

    Where the parameters are:
        file_name: Name of the file containing the iris dataset.
    """
    # Load the dataset
    df = load_dataset(file_name)

    # Summary of the variables

    # Types of Variables of the Dataset
    # Create a string buffer to capture the output
    variable_buffer = io.StringIO()
    # Capture the output of df.info()
    df.info(buf=variable_buffer)

    # Categorical Data
    categorical_summary = {}
    # Count: loop through each categorical variables
    for column in df.select_dtypes(include=['object']):
        # Count occurrences of each category
        counts = df[column].value_counts()
        # Get the number of unique categories
        unique_categories = len(counts)
        # Add summary to dictionary
        categorical_summary[column] = {
            'count': counts,
            'unique_categories': unique_categories
        }

    # Continuous Data
    # Calculate continuous summary
    continuous_summary = df.describe()

    # Output to a single text file
    with open('summary.txt', 'wt') as sf:
        # Write the title of the summary.txt file
        sf.write("This is a summary of the Iris Dataset variables:\n\n\n")

        # Write an overview of the first 5 rows of the dataset
        sf.write("1. Introduction: Looking into the data\n\n")
        sf.write("1.1 Head of the Dataset:\n")
        sf.write("This is a quick overview of the first 5 rows of the dataset.\n")
        sf.write(df.head().to_string() + "\n\n")

        # Write an overview of the last 5 rows of the dataset
        sf.write("1.2 Tail of the Dataset:\n")
        sf.write("This is a quick overview of the last 5 rows of the dataset.\n")
        sf.write(df.tail().to_string() + "\n\n\n")

        # Introduce the types of variables in the dataset
        sf.write('2. Summary of the Data Types in Python:\n\n')
        # Write the captured output of df.info() to the file
        sf.write(variable_buffer.getvalue())
        # Write the variable types and their corresponding types
        sf.write('\n2.1 Variables Types Classification based on Python Data Types: \n\nobject = Categorical Variable \nfloat64 = Continuous Variable\n\n\n')

        # Write summaries for categorical variables
        sf.write("3. Summary for Categorical Variables:\n\n")
        # Initialize the counter for variable numbering
        counter = 1
        # Iterate through each categorical variable and its summary
        for variable, summary in categorical_summary.items():
            # Write the variable name and its index
            sf.write(f"3.{counter} Variable: {variable}\n")
            # Write the count of each category without headers
            sf.write(summary['count'].to_string(header=False))
            # Write the number of unique categories
            sf.write(f"\n\nUnique Categories: {summary['unique_categories']}\n\n\n")
            # Increment the counter for the next variable
            counter += 1 

        # Write summary for continuous variables
        sf.write("4. Summary for Continuous Variables:\n\n")
        # Initialize the counter for variable numbering
        counter = 1
        # Iterate through each continuous variable
        for column in continuous_summary.columns:
            # Write the variable name and its index
            sf.write(f"4.{counter} Variable: {column}\n")
            # Iterate through each statistical measure for the variable
            for statistic in continuous_summary.index:
                # Write the statistic name and its corresponding value
                sf.write(f"{statistic.capitalize()}: {continuous_summary.loc[statistic, column]}\n")
            # Add a newline after writing all statistics for a variable
            sf.write("\n")
            # Increment the counter for the next variable
            counter += 1

        # Generate a summary of correlation analysis and write it to summary.txt
        sf.write("\n5. Summary of Correlation Analysis:\n\n")
        # Call create_correlation function to compute correlation analysis
        correlation_output = create_correlation(file_name)
        # Write the correlation analysis output to the summary file
        sf.write(correlation_output)

# If this script is executed as the main program,
# Generate a summary for the 'iris.data' dataset
if __name__ == "__main__":
    create_summary('iris.data')
