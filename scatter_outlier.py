import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    dataframe = pd.read_csv("100 Records.csv")
    # data has all records using salary and age
    x = dataframe['Salary']
    y = dataframe['Age in Yrs.']
    # scatter plot, first method is to observe plot
    plt.scatter(x, y)
    plt.show()
    # outliers for salary, x :
    # z method for outlier z = (observation - mean)/standard deviation, anything > than 3 quartile is outlier
    outliers1 = []
    mean = np.mean(x)
    std_dev = np.std(x)
    threshold_value = 3
    for y in x:
        z = (y - mean) / std_dev
        if np.abs(z) > z:
            outliers1.append(y)
    print("Outliers using 1st method are:", outliers1)
    # IQR method, values greater than 1.5 times the third quartile are outliers
    # first, sort in ascending order
    sorted(x)
    # calculate first and third quartile and find range
    q1, q3 = np.percentile(x, [25, 75])  # (array, percentage)
    iqr = q3 - q1  # diff b/w third and first quartile, gives range
    # lower and upper bound
    lower_bound = (1.5 * iqr) - q1
    upper_bound = q3 + (1.5 * iqr)
    outliers2 = []
    for y in x:
        if y > upper_bound or y < lower_bound:
            outliers2.append(y)
    print("Outliers using 2nd method are:", outliers2)