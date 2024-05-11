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
# Import 'io' to use a string buffer for df.info()
import io

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
column_title = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"]

# Setting column titles as headers to the dataframe
df.columns = column_title

# Print the first 5 rows of the DataFrame
# print(df.head())


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
   