import pandas as pd

data = {
    'Employee': ['Ravi', 'Priya', 'Anil', 'Neha', 'Karan', 'Meena', 'Amit', 'Divya'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [90000, 60000, 75000, 50000, 30000, 85000, 45000, 99000],
    'Experience': [5, 3, 6, 2, 1, 7, 4, 10]
}

df = pd.DataFrame(data)

group_df=df.groupby("Department").filter(lambda g: g["Salary"].mean()>70000)
print(group_df)