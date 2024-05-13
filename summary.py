# Program: summary.py
# This program: 1. Outputs a summary of each variable to a single text file.
# Author: Filipe Carvalho


# Import necessary libraries

# Import 'pandas' for the data summary
import pandas as pd
# Import 'io' to use a string buffer for df.info()
import io
# Import the load_dataset function from load_iris.py
from load_iris import load_dataset

from correlation import create_correlation  # Import create_correlation function

def create_summary(file_name):
    
    # Load the dataset
    df = load_dataset(file_name)
    
    # Summary of the variables

    # Types of Variables of the Dataset
    # Creating a string buffer to capture the output
    variable_buffer = io.StringIO()
    # Capturing the output of df.info()
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
        # Writing the title of the summary.txt file
        sf.write("This is a summary of the Iris Dataset variables:\n\n\n")

        # Introducing the types of variables in the dataset
        sf.write('1. Introduction - Summary of the Data Types in Python:\n\n')
        # Writing the captured output of df.info() to the file
        sf.write(variable_buffer.getvalue())
        # Writing the variable types and their corresponding types
        sf.write('\n\n2.Variables Types Classification based on Python Data Types: \n\nobject = Categorical Variable \nfloat64 = Continuous Variable')


        # Write summary for categorical variables
        sf.write("\n\n\n3. Summary for Categorical Variables:\n\n")
        # Initialize the counter
        counter = 1
        for variable, summary in categorical_summary.items():
            # Write the variable name before its summary
            sf.write(f"3.{counter} Variable: {variable}\n")
            sf.write(summary['count'].to_string(header=False))
            sf.write(f"\n\nUnique Categories: {summary['unique_categories']}\n\n\n")
            # Iterating in each loop
            counter += 1 

        # Write summary for continuous variables
        sf.write("4. Summary for Continuous Variables:\n\n")
        # Initialize the counter
        counter = 1
        for column in continuous_summary.columns:
            sf.write(f"4.{counter} Variable: {column}\n")
            for statistic in continuous_summary.index:
                sf.write(f"{statistic.capitalize()}: {continuous_summary.loc[statistic, column]}\n")
            sf.write("\n")
            # Iterating in each loop
            counter += 1

        # Call create_correlation and write its output to summary.txt
        sf.write("\n5. Summary of Correlation Analysis:\n\n")
        correlation_output = create_correlation(file_name)
        sf.write(correlation_output)

if __name__ == "__main__":
    create_summary('iris.data')