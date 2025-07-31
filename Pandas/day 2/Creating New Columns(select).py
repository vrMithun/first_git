import pandas as pd
import numpy as np
data = {
    'Employee': ['Ravi', 'Priya', 'Anil', 'Neha', 'Karan', 'Meena', 'Amit', 'Divya'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [90000, 60000, 75000, 50000, 30000, 85000, 45000, 99000],
    'Experience': [5, 3, 6, 2, 1, 7, 4, 10]
}

df = pd.DataFrame(data)
'''Create a new column "Seniority" based on both Salary and Experience:
Condition	                    Seniority
Experience ≥ 7 and Salary ≥ 90000	"Very Senior"
Experience ≥ 5 and Salary ≥ 70000	"Senior"
Experience ≥ 3 and Salary ≥ 50000	"Mid-Level"
Else	"Junior"'''
condition=[(df["Experience"]>=7) & (df["Salary"]>=90000),(df['Experience']>=5) & (df['Salary']>=70000),\
           (df['Experience']>=3) & (df["Salary"]>=50000),(df['Experience']<3) | (df['Salary']<50000)]
value=["Very Senior","Senior","Mid-Level","Junior"]

df["Seniority"]=np.select(condition,value)
print(df["Seniority"])