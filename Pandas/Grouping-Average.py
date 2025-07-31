import pandas as pd

"""
Group the DataFrame by the "Department" column and compute the average salary for each department. 
Output should be a new DataFrame with:

        i)Department
       ii)Average_Salary
"""

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'Salary': [50000, 60000, 52000, 58000, 62000, 60000]
}

df = pd.DataFrame(data)
grouped=df.groupby(by="Department")["Salary"].mean().reset_index()
grouped.rename(columns={"Salary":"AvgSalary"},inplace=True)
print(grouped.head())