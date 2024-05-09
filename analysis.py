# Program: analysis.py
# This program:
#   1. Outputs a summary of each variable to a single text file,
#   2. Saves a histogram of each variable to png files, and
#   3. Outputs a scatter plot of each pair of variables.
#   4. Performs any other analysis you think is appropriate.
# Author: Filipe Carvalho

# Part 1: Outputs a summary of each variable to a single text file

# Import os to check if the file exists
import os

# Assign the iris dataset to a variable
file_name = 'iris.data'

# Check if file exists
if os.path.exists(file_name):
    # if file exists, then load the iris dataset
    with open (file_name, 'r') as df:
        data = df.read()
else:
    # if file does not exist, then output a message
    print(f'{file_name} does not exist')


# Output to a single text file
with open ('summary.txt','wt') as sf:
    sf.write('summary')
# print ('done')