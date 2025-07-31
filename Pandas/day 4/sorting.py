import pandas as pd

data = {
    'Employee': ['Ravi', 'Priya', 'Anil', 'Neha', 'Karan', 'Meena', 'Amit', 'Divya'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [90000, 60000, 75000, 50000, 30000, 85000, 45000, 99000],
    'Experience': [5, 3, 6, 2, 1, 7, 4, 10]
}

df = pd.DataFrame(data)
'''
Sort the DataFrame by:
Salary in descending order
'''

sorted_df=df.sort_values(by="Salary",ascending=False).reset_index(drop=True)
print(sorted_df)