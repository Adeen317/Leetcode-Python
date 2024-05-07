import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    duplicate = customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers
 
    
