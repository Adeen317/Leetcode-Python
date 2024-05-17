import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    man = employee.groupby('managerId').apply(lambda x: x['id'].count())
    
    managers = man[man >= 5].index

    result = employee[employee['id'].isin(managers)]['name'].reset_index(drop=True)
    return pd.DataFrame(result)
        
