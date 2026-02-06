import pandas as pd

'''
    Select the top 5 students with the highest scores.

    From these top 5, display only the "Name" and "Score" columns.
'''

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Score': [85, 92, 78, 90, 88, 76, 95, 89],
    'Passed': [True, True, False, True, True, False, True, True]
}

df = pd.DataFrame(data)

filtered_df=df.sort_values(by="Score",ascending=False,inplace=False)
print(filtered_df[["Name","Score"]].head())