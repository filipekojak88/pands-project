# Program: scatterplot.py
# This program: 3. Outputs a scatter plot of each pair of variables.
# Author: Filipe Carvalho


# Import necessary libraries

# Import the load_dataset function from load_iris.py
from load_iris import load_dataset

import matplotlib.pyplot as plt

import seaborn as sns

def create_scatterplot (file_name):
    
    # Load the dataset
    df = load_dataset(file_name)

    # Extract continuous variable names
    continuous_vars = df.columns[:-1]  # Exclude the last column which is categorical
    
    # Create scatterplot matrix with seaborn pairplot
    sns.pairplot(df, vars=continuous_vars, hue='Species')
    plt.show()

if __name__ == "__main__":
    create_scatterplot('iris.data')