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
   
# 2: Saves a histogram of each variable to png files
        
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, skew

# Load through each continuous variable
for column_name, data in df.select_dtypes(include=['float64']).items():
    # Calculate histogram with specified number of bins
    num_bins = 15
    counts, bin_edges = np.histogram(data, bins=num_bins)

    # Plot histogram using plt.bar() with bin edges and counts
    plt.bar(bin_edges[:-1], counts, width=np.diff(bin_edges), color='blue', edgecolor='black', linewidth=1.2, label=f'Histogram')

    # Add title and labels
    plt.title(f"Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")

    # Calculate positions for tick labels at bin edges
    tick_positions = bin_edges  # Use bin edges as tick positions

    # Set custom x-axis tick positions and labels
    plt.xticks(tick_positions, labels=[f"{bin_edge:.1f}" for bin_edge in bin_edges], rotation=45, fontsize=8)

    # Calculate skewness
    skewness = skew(data)
    # print(skewness) - to confirm the skewness as the histograms are plotted.

    if abs(skewness) < 0.5:  # If skewness is close to zero, consider it approximately normal
        # Fit a normal distribution to the data
        mu, std = norm.fit(data)  # Estimate mean (mu) and standard deviation (std) of the data

        # Generate x values for the normal distribution curve
        x = np.linspace(min(data), max(data), 100)
        pdf = norm.pdf(x, mu, std)  # Calculate the probability density function (PDF) for the normal distribution

        # Plot the normal distribution curve (bell-shaped line)
        plt.plot(x, pdf * len(data) * np.diff(bin_edges)[0], 'r-', linewidth=2, label='Normal Distribution')

    else:  # If skewness is not close to zero, add a line representing skewness
        plt.axvline(np.mean(data) + np.std(data), color='green', linestyle='dashed', linewidth=2, label='Skewness Line')

    # Calculate the mean and median of the data
    mean_depth = np.mean(data)
    median_depth = np.median(data)

    # Add vertical lines at the mean and median values
    plt.axvline(mean_depth, color='green', linestyle='dashed', linewidth=2, label=f'Mean {column_name}')
    plt.axvline(median_depth, color='gray', linestyle='dashed', linewidth=2, label=f'Median {column_name}')

    # Create legend handles and labels for different groups of legends
    handles, labels = plt.gca().get_legend_handles_labels()

    # Create legend for left side (Histogram and Normal Distribution)
    left_legend = plt.legend(handles[:2], labels[:2], loc='upper left')

    # Create legend for right side (Mean Depth and Median Depth)
    right_legend = plt.legend(handles[2:], labels[2:], loc='upper right')

    # Add both legends to the plot
    plt.gca().add_artist(left_legend)
    plt.gca().add_artist(right_legend)

    # Save the histogram as a PNG file
    plt.savefig(f"{column_name}_histogram.png")
    plt.close()  # Close the current figure to release memory and avoid overlapping plots
