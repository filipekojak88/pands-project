# Program: analysis.py
# This program:
#   1. Outputs a summary of each variable to a single text file,
#   2. Saves a histogram of each variable to png files, and
#   3. Outputs a scatter plot of each pair of variables.
#   4. Performs any other analysis you think is appropriate.
# Author: Filipe Carvalho

# 1: Outputs a summary of each variable to a single text file

# Import 'os' to check if the file exists
import os
# Import 'pandas' for the data summary
import pandas as pd

# Assign the iris dataset to a variable
file_name = 'iris.data'

# Check if file exists
if os.path.exists(file_name):
    # if file exists, then load the iris dataset using pandas
    df = pd.read_csv(file_name, header=None)
else:
    # if file does not exist, then output a message
    print(f'{file_name} does not exist. The "iris.data" file needs to be saved in the repository pands-project')

# Adding Column titles to the iris.data
# Defining the column titles
column_title = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"]

# Setting column titles as headers to the dataframe
df.columns = column_title

# Print the first 5 rows of the DataFrame
# print(df.head())


# Summary of the variables

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
    sf.write(f"This is the summary of the variables in Iris Dataset:\n\n")
    # Write summary for continuous variables
    sf.write("Summary for Continuous Variables:\n")
    for column in continuous_summary.columns:
        sf.write(f"Variable: {column}\n")
        for statistic in continuous_summary.index:
            sf.write(f"{statistic.capitalize()}: {continuous_summary.loc[statistic, column]}\n")
        sf.write("\n")
    
    # Write summary for categorical variables
    sf.write("Summary for Categorical Variables:\n")
    for variable, summary in categorical_summary.items():
        sf.write(f"Variable: {variable}\n")
        sf.write(summary['count'].to_string())
        sf.write(f"\nUnique Categories: {summary['unique_categories']}\n\n")