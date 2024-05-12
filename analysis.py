# Program: analysis.py
# This program:
#   1. Outputs a summary of each variable to a single text file,
#   2. Saves a histogram of each variable to png files, and
#   3. Outputs a scatter plot of each pair of variables.
#   4. Performs any other analysis you think is appropriate.
# Author: Filipe Carvalho


# Import necessary libraries

from summary import create_summary

from histogram import create_histogram

from scatterplot import create_scatterplot

# 1: Outputs a summary of each variable to a single text file
create_summary('iris.data')
   
# 2: Saves a histogram of each variable to png files
create_histogram('iris.data')

# 3: Outputs a scatter plot of each pair of variables
create_scatterplot('iris.data')

