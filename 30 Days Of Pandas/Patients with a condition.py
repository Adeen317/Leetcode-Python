import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patient=patients[(patients['conditions'].str.contains(' DIAB1'))|(patients['conditions'].str.startswith('DIAB1'))]
    return patient
    
