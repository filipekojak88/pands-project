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

from heatmap import create_heatmap

file_name = 'iris.data'

# 1: Outputs a summary of each variable to a single text file
create_summary(file_name)
   
# 2: Saves a histogram of each variable to png files
create_histogram(file_name)

# 3: Outputs a scatter plot of each pair of variables
create_scatterplot(file_name)

# 4: Outputs a heatmap with the correlation between the pair of variables
create_heatmap(file_name)

# 5: Outputs a correlation analysis of the correlation coefficient between the pair of variables.
# correlation.py was created and added as a module in summary.py to be printed to summary.txt.