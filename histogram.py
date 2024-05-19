# Program: histogram.py
# This program: 2. Saves a histogram of each variable to png files
# Author: Filipe Carvalho


# Import necessary libraries

# Custom function to load the iris dataset from a file
from load_iris import load_dataset
# Module for creating and saving histograms and other plots
import matplotlib.pyplot as plt
# Module for numerical operations and array manipulation, used for histogram calculations
import numpy as np
# Used for fitting normal distributions and calculating skewness in the histograms
from scipy.stats import norm, skew
# Used for creating directories and saving histogram images
import os

def create_histogram (file_name):
    """
    Create histograms for continuous variables in the dataset.

    Args:
    file_name (str): Name of the file containing the dataset.

    """
    
    # Load the dataset
    df = load_dataset(file_name)

    # Create directory if it doesn't exist
    os.makedirs("histogram", exist_ok=True)

    # Iterate through each continuous variable in the dataset
    for column_name, data in df.select_dtypes(include=['float64']).items():
        # Calculate histogram with specified number of bins
        num_bins = 15
        # Store the counts of data points in each bin and bin edges
        counts, bin_edges = np.histogram(data, bins=num_bins)

        # Plot histogram using plt.bar() with bin edges and counts
        plt.bar(bin_edges[:-1], counts, width=np.diff(bin_edges), color='blue', edgecolor='black', linewidth=1.2, label=f'Histogram')

        # Add title and labels
        plt.title(f"Distribution of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")

        # Calculate positions for tick labels at bin edges
        tick_positions = bin_edges  

        # Set custom x-axis tick positions and labels
        plt.xticks(tick_positions, labels=[f"{bin_edge:.1f}" for bin_edge in bin_edges], rotation=45, fontsize=8)

        # Calculate skewness of the data
        skewness = skew(data)
        
        # Check if data is approximately normal or skewed
        if abs(skewness) < 0.5:   
            # Fit a normal distribution to the data, estimating mean (mu) and standard deviation (std) of the data
            mu, std = norm.fit(data)

            # Generate x values for the normal distribution curve
            x = np.linspace(min(data), max(data), 100)
            # Calculate the probability density function (PDF) for the normal distribution
            pdf = norm.pdf(x, mu, std)  

            # Plot the normal distribution curve (bell-shaped line)
            plt.plot(x, pdf * len(data) * np.diff(bin_edges)[0], 'r-', linewidth=2, label='Normal Distribution')

        # if data is not approximately normal 
        else:   
            # Add a line representing skewness           
            plt.axvline(np.mean(data) + np.std(data), color='green', linestyle='dashed', linewidth=2, label='Skewness Line')

        # Calculate the mean of the data
        mean = np.mean(data)
        # Calculate the median of the data
        median = np.median(data)

        # Add vertical lines at the mean and median values
        plt.axvline(mean, color='green', linestyle='dashed', linewidth=2, label=f'Mean {column_name}')
        plt.axvline(median, color='gray', linestyle='dashed', linewidth=2, label=f'Median {column_name}')

        # Create legend handles and labels for different groups of legends
        handles, labels = plt.gca().get_legend_handles_labels()

        # Create legend for left side (Histogram and Normal Distribution)
        left_legend = plt.legend(handles[:2], labels[:2], loc='upper left')

        # Create legend for right side (Mean Depth and Median Depth)
        right_legend = plt.legend(handles[2:], labels[2:], loc='upper right')

        # Add both legends to the plot
        plt.gca().add_artist(left_legend)
        plt.gca().add_artist(right_legend)

        # Save the histogram as a PNG file within the histogram directory
        plt.savefig(os.path.join("histogram",f"{column_name}_histogram.png"))
        # Close the current figure to release memory and avoid overlapping plots
        plt.close()  

# If this script is executed as the main program
if __name__ == "__main__":
     # Creates histograms for the 'iris.data' dataset 
    create_histogram('iris.data')