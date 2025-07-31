import pandas as pd

data = {
    'Name': ['Anya', 'Ben', 'Catherine', 'Derek', 'Eva'],
    'Age': [28, 34, 29, 42, 31],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [52000, 75000, 62000, 88000, 58000]
}

df = pd.DataFrame(data)

# 1)Select all employees whose salary is greater than 60000.
fdf=df[(df["Salary"]>60000)]
print(fdf["Name"])
# 2)Select all employees from the HR department who are older than 30.
fdf=df[(df["Age"]>30) & (df["Department"]=="HR")]
print(fdf["Name"])
# 3)Select rows where the department is not IT.
fdf=df[(df["Department"]!="IT")]
print(df.to_string())
# 4)Display only the names of employees earning above 70000.
fdf=df[(df['Salary']>70000)].reset_index()
print(fdf["Name"])