import pandas as pd

def nth_highest_salary(df: pd.DataFrame, N: int) -> pd.DataFrame:
    if N<=0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
        
    sorted_df = df.sort_values(by='salary', ascending=False)
    #print(sorted_df)
    
    # Remove Duplicate
    unique_salaries = sorted_df['salary'].unique()
    
    # If there are less than two unique salaries than return None
    if len(unique_salaries) >= N:
        return pd.DataFrame({f"getNthHighestSalary({N})": [unique_salaries[N-1]]})
    
    else:
        # Return the second highest salary as a DataFrame
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
