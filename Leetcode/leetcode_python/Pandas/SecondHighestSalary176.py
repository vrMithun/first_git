import pandas as pd
import numpy as np
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_df=employee.sort_values(by="salary",ascending=False).reset_index(drop=True)
    unique_col=sorted_df["salary"].unique()
    unique_col.sort()
    if (len(sorted_df)<2) or (len(unique_col)==1):
        return pd.DataFrame({"SecondHighestSalary": [np.nan]})
    salary=unique_col[-2]
    result_df = pd.DataFrame({"SecondHighestSalary": [salary]})
    return result_df
    