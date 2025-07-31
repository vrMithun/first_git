import pandas as pd

data = {
    'Employee': ['Ravi', 'Priya', 'Anil', 'Neha', 'Karan', 'Meena', 'Amit', 'Divya'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [90000, 60000, 75000, 50000, 30000, 85000, 45000, 99000],
    'Experience': [5, 3, 6, 2, 1, 7, 4, 10]
}

df = pd.DataFrame(data)
#Find all departments where the average salary is greater than ₹70,000.

avg_salary = df.groupby("Department")["Salary"].mean().reset_index()
avg_salary = avg_salary[avg_salary["Salary"] > 70000]

# Step 2: Filter original df based on those departments
high_salary_departments = avg_salary["Department"]
result = df[df["Department"].isin(high_salary_departments)]

print(result)