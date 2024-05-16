# Program: histogram.py
# This program: 2. Saves a histogram of each variable to png files
# Author: Filipe Carvalho


# Import necessary libraries

# Import the load_dataset function from load_iris.py
from load_iris import load_dataset

import matplotlib.pyplot as plt

import numpy as np

from scipy.stats import norm, skew

import os

def create_histogram (file_name):
    
    # Load the dataset
    df = load_dataset(file_name)

    # Create directory if it doesn't exist
    os.makedirs("histogram", exist_ok=True)

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

        # Save the histogram as a PNG file within the histogram directory
        plt.savefig(os.path.join("histogram",f"{column_name}_histogram.png"))
        plt.close()  # Close the current figure to release memory and avoid overlapping plots

if __name__ == "__main__":
    create_histogram('iris.data')