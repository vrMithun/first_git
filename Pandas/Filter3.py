import pandas as pd

'''
Group the data by "Student".

Calculate the average score for each student.

Filter only the students with an average score ≥ 85.

Sort the result in descending order of average score.

👉 Output should contain: "Student" and "Average_Score".

'''

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'Math', 'Science'],
    'Score': [85, 90, 78, 92, 88, 84, 75, 95]
}

df = pd.DataFrame(data)

grouped=df.groupby(by="Student")["Score"].mean().reset_index()
grouped.rename(columns={"Score":"AverageScore"},inplace=True)
grouped.sort_values(by="AverageScore",ascending=False,inplace=True)
print(grouped[(grouped["AverageScore"]>=85)].to_string())