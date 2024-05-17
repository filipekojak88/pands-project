# Program: analysis.py
# Description:
#   This program conducts comprehensive analysis on a dataset including:
#   1. Generating a summary of each variable to a single text file,
#   2. Saving histograms of each variable to PNG files,
#   3. Creating scatter plots of each pair of variables,
#   4. Constructing a heatmap illustrating the correlation between variables, and
#   5. Performing additional correlation analysis between variable pairs (executed by the function create_summary())
# Author: Filipe Carvalho

# Import necessary libraries

from summary import create_summary

from histogram import create_histogram

from scatterplot import create_scatterplot

from heatmap import create_heatmap


# File containing the dataset
file_name = 'iris.data'

# 1: Outputs a summary of each variable to a single text file
create_summary(file_name)
   
# 2: Saves a histogram of each variable to PNG files
create_histogram(file_name)

# 3: Outputs a scatter plot of each pair of variables
create_scatterplot(file_name)

# 4: Outputs a heatmap with the correlation between the pair of variables
create_heatmap(file_name)
