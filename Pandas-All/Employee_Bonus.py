import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    merge = pd.merge(employee, bonus, on='empId', how='left')

    result=merge[(merge['bonus']<1000) | (merge['bonus'].isnull())]

    return result[['name','bonus']]
    
