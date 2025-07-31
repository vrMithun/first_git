import pandas as pd

'''
Filter employees who:

Work in the IT department

Have Salary > 70000

Have Experience ≥ 5 years

From these filtered rows, display only "Name", "Salary", and "Experience" sorted by Salary descending.
'''

data = {
    'Name': ['Ravi', 'Priya', 'Anil', 'Neha', 'Karan', 'Meena', 'Amit', 'Divya'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Salary': [48000, 75000, 60000, 82000, 50000, 62000, 79000, 51000],
    'Experience': [2, 6, 4, 7, 3, 5, 6, 2]
}
df = pd.DataFrame(data)
filtered=df[(df["Department"]=='IT') & (df["Salary"]>70000) & (df["Experience"]>=5)]

print(filtered[["Name","Salary","Experience"]].sort_values(by="Salary",ascending=False))