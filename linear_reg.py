import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

if __name__ == '__main__':
    dataframe = pd.read_csv("100 Records.csv")
    # data has all records using salary and age
    x = dataframe['Salary']
    y = dataframe['Age in Yrs.']
    # scatter plot
    plt.scatter(x, y)
    # linear regression
    stats = linregress(x, y)
    m = stats.slope
    c = stats.intercept
    plt.xlabel("Salary", fontsize=20)
    plt.ylabel("Age(in Yrs)", fontsize=20)
    plt.plot(x, m * x + c, color="red", linewidth=3)
