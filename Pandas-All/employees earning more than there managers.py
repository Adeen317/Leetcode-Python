import pandas as pd

def find_employees(df: pd.DataFrame) -> pd.DataFrame:
    # Merge the DataFrame with itself on ManagerId to compare salaries
    merged_df = pd.merge(df, df, left_on='managerId', right_on='id', suffixes=('_employee', '_manager'))
    
    # Filter rows where employee's salary is greater than manager's salary
    result_df = merged_df[merged_df['salary_employee'] > merged_df['salary_manager']]
    
    
    return pd.DataFrame({"Employee": [result_df['name_employee']]})
    
    
