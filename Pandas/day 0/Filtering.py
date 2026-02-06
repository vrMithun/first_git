import pandas as pd

'''
Filter the rows where:
    Salary is greater than or equal to 58000
    Experience is more than 4 years

Then:
    Sort the filtered rows by "Experience" in descending order
'''

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'Salary': [50000, 60000, 52000, 58000, 62000, 60000],
    'Experience': [2, 5, 3, 7, 4, 6]
}

df = pd.DataFrame(data)
filtered_df=df[(df["Salary"]>=58000) & (df["Experience"]>4)].sort_values(by="Experience",ascending=False)
print(filtered_df.to_string())

