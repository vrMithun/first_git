import pandas as pd

'''
Filter the students who:

    Scored above 85

    Passed the test

    Had at most 2 attempts

From this filtered data, show only "Name", "Score", and "Attempts", sorted by Score (descending).
'''

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Score': [85, 92, 78, 90, 88, 76, 95, 89],
    'Passed': [True, True, False, True, True, False, True, True],
    'Attempts': [1, 2, 3, 1, 2, 3, 1, 2]
}

df = pd.DataFrame(data)

filtered=df[(df["Score"]>85) & (df["Passed"]==True) & (df["Attempts"]<=2)].sort_values(by="Score",ascending=False)
print(filtered[["Name","Score","Attempts"]].to_string())