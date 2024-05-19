# Program: analysis.py
# This program conducts comprehensive analysis on a dataset including:
#   1. A summary of each variable generated to a single text file,
#   2. Histograms of each variable saved to PNG files,
#   3. Scatter plots of each pair of variables,
#   4. Heat map illustrating the correlation between variables, and
#   5. Additional correlation analysis between variable pairs, executed by the function create_summary.
# Author: Filipe Carvalho


# Import necessary libraries:

# Import the 'create_summary' function from the customized 'summary' module.
from summary import create_summary
# Import the 'create_histogram' function from the customized 'histogram' module.
from histogram import create_histogram
# Import the 'create_scatterplot' function from the customized 'scatterplot' module.
from scatterplot import create_scatterplot
# Import the 'create_heatmap' function from the customized 'heatmap' module.
from heatmap import create_heatmap

# Assign the Iris DataSet 'iris.data' to a variable file_name
file_name = 'iris.data'


# Pass the variable representing 'iris.data' as an argument within the functions below and execute them.

# 1: Outputs a summary of each variable to a single text file
create_summary(file_name)
   
# 2: Saves a histogram of each variable to PNG files
create_histogram(file_name)

# 3: Outputs a scatter plot of each pair of variables
create_scatterplot(file_name)

# 4: Outputs a heatmap with the correlation between the pair of variables
create_heatmap(file_name)
