import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
print(df)
# 1)What is the shape of the DataFrame?
print("shape of the data frame is:",df.shape)

# 2)Display only the Name and Department columns.
print(df[["Name","Department"]])

# 3)Display the first two rows.
print(df.head(2))

# 4)How many unique departments are there?
print(df["Department"].unique())
