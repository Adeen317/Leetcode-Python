import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merge = pd.merge(employee, department, left_on='departmentId', right_on='id')

    merge=merge.groupby('name_y').apply(lambda x: x[x['salary'] == x['salary'].max()][['name_y','name_x', 'salary']])

    merge=merge[['name_y', 'name_x', 'salary']].rename(columns={'name_y': 'Department', 'name_x': 'Employee','salary':'Salary'}).reset_index(drop=True)

    return merge
    
