import pandas as pd

data = {
    'Employee': ['Ravi', 'Priya', 'Anil', 'Neha', 'Karan', 'Meena', 'Amit', 'Divya'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [90000, 60000, 75000, 50000, 30000, 85000, 45000, 99000],
    'Experience': [5, 3, 6, 2, 1, 7, 4, 10]
}

df = pd.DataFrame(data)

gdf=df.groupby(by="Department")["Salary"].mean().reset_index()
gdf.rename(columns={"Salary":"Avg Salary"},inplace=True)
print(gdf.to_string())

"""
👉 For each department, find:
Average Experience
Minimum Salary
Maximum Salary
"""
multi_gdf=df.groupby("Department").agg(
    avg_exp=("Experience",'mean'),
    min_salary=("Salary",'min'),
    max_salary=("Salary",'max')
).reset_index()

print(multi_gdf.to_string())