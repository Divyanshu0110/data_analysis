import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    dataframe = pd.read_csv("100 Records.csv")
    # data has all records using salary and age
    x = dataframe['Salary']
    y = dataframe['Age in Yrs.']
    z = dataframe['City']
    # scatter plot for x and y
    plt.scatter(x, y)
    # histogram for x and y
    plt.hist(x, y, color="blue")
    # pie chart for z
    plt.show()