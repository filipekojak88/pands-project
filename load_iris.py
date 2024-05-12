# Program: load_iris.py
# This program: Loads the iris dataset.
# Author: Filipe Carvalho

# Import necessary libraries

# Import 'os' to check if the file exists
import os
# Import 'pandas' for the data summary
import pandas as pd


def load_dataset(file_name):
    # Check if file exists
    if not os.path.exists(file_name):
        # if file does not exist, then output a message
        print(f'{file_name} does not exist. The "iris.data" file needs to be saved in the repository pands-project')
        quit(1)
    
    # Load dataset 
    df = pd.read_csv(file_name, header=None)

    # Adding Column titles to the iris.data
    # Defining the column titles
    column_title = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"]

    # Setting column titles as headers to the dataframe
    df.columns = column_title

    # Print the first 5 rows of the DataFrame
    print(df.head())

    # Load dataset and return it
    return df
    
if __name__ == "__main__":
    load_dataset ('iris.data')