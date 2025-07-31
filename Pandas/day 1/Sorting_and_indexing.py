import pandas as pd

data = {
    'Name': ['Isha', 'John', 'Kiran', 'Leah', 'Manav'],
    'Age': [27, 45, 31, 29, 38],
    'Department': ['Sales', 'IT', 'HR', 'IT', 'Finance'],
    'Salary': [51000, 86000, 64000, 72000, 60000]
}

df = pd.DataFrame(data)

# Sort the DataFrame by Salary in descending order.
Sort_df=df.sort_values(by="Salary",ascending=False,inplace=False)
print(Sort_df.to_string())
# Sort the DataFrame first by Department (ascending) and then by Age (descending).
sort_df=df.sort_values(by=["Department","Age"],ascending=[True,False]).reset_index()
print(sort_df.to_string())
# Reset the index after sorting by salary.
Sort_df=df.sort_values(by="Salary",ascending=False,inplace=False).reset_index()
print(Sort_df.to_string())
# Set the Name column as the index of the DataFrame.
#df.set_index(df["Name"])
df.set_index("Name",inplace=True)
# After setting Name as index, retrieve the row for 'Leah'.
print(df.loc["Leah"])