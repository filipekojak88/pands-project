# Program: analysis.py
# This program:
#   1. Outputs a summary of each variable to a single text file,
#   2. Saves a histogram of each variable to png files, and
#   3. Outputs a scatter plot of each pair of variables.
#   4. Performs any other analysis you think is appropriate.
# Author: Filipe Carvalho

# Part 1: Outputs a summary of each variable to a single text file

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

# Output to a single text file
with open ('summary.txt','wt') as sf:
    sf.write('summary')
# print ('done')