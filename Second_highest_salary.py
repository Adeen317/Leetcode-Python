import pandas as pd

def second_highest_salary(df: pd.DataFrame) -> pd.DataFrame:
    sorted_df = df.sort_values(by='salary', ascending=False)
    #print(sorted_df)
    
    # Remove Duplicate
    unique_salaries = sorted_df['salary'].unique()
    
    # If there are less than two unique salaries than return None
    if len(unique_salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    
    # Return the second highest salary as a DataFrame
    return pd.DataFrame({"SecondHighestSalary": [unique_salaries[1]]})
