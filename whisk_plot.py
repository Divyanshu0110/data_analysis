import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    dataframe = pd.read_csv("100 Records.csv")
    # data has all records using salary and age
    x = dataframe['Salary']
    # box and whisker plot
    plt.boxplot(x, vert=0)
    plt.show()
    # five number summary includes min, max, median, 1st and 3rd quartile
    min_value = min(x)
    max_value = max(x)
    median = np.median(x)
    q1, q3 = np.percentile(x, [25, 75])
    print("Min:", min_value, ", Max:", max_value, ", Median:", median, ", First quartile:", q1, ", Third quartile:", q3)
