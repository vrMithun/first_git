import pandas as pd
import numpy as np

"""
Drop rows where the Salary is missing.

Fill missing values in the Experience column with the mean experience.

Print the cleaned DataFrame.
"""

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Salary': [50000, np.nan, 52000, 58000, 62000, np.nan],
    'Experience': [2, 5, 3, np.nan, 4, 6]
}

df = pd.DataFrame(data)
non_empty_df=df.dropna(subset="Salary")
non_empty_df["Experience"]=non_empty_df["Experience"].fillna(non_empty_df["Experience"].mean())
print(non_empty_df.to_string())
