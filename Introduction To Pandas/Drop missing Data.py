import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    drop= students.dropna(subset=['name'], inplace=True)
    return students
    
