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

def condition(row):
    Exp=row["Experience"]
    Sal=row["Salary"]
    if Exp>=7 and Sal>=90000:
        return "Very Senior"
    elif Exp>=5 and Sal>=70000:
        return "Senior"
    elif Exp>=3 and Sal>=50000:
        return "Mid-Level"
    else:
        return "Junior"
    
df["Seniority"]=df.apply(condition,axis=1)
print(df["Seniority"])