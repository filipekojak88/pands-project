# Program: scatterplot.py
# This program outputs a scatter plot of each pair of variables.
# Author: Filipe Carvalho


# Import necessary libraries

# Import the load_dataset function from custom load_iris.py module 
from load_iris import load_dataset
# Import matplotlib for plotting
import matplotlib.pyplot as plt
# Import seaborn for scatterplot visualization
import seaborn as sns

def create_scatterplot (file_name):
    """
    Creates a scatterplot matrix for the given dataset file.

    Parameter:
        file_name (str): Name of the file containing the Iris DataSet.
    """
    # Load the dataset
    df = load_dataset(file_name)

    # Extract continuous variable names
    continuous_vars = []
    # Iterate through each column in the DataFrame
    for column_name, data in df.items():
        # Check if data type is float64
        if data.dtype == 'float64':  # Check if data type is float64
            # If the data type is float64, add the column name to the list of continuous variables
            continuous_vars.append(column_name)
    
    # Create scatterplot matrix with seaborn pairplot
    sns.pairplot(df, vars=continuous_vars, hue='Species')
    # Display the scatterplot matrix
    plt.show()

# If this script is executed as the main program
if __name__ == "__main__":
    # Execute the function create_scatterplot using the 'iris.data' dataset as an argument
    create_scatterplot('iris.data')