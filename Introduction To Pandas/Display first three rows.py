import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    f=employees.head(3)
    return f
    
