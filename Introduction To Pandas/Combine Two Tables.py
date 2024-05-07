import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    # Perform left merge
    merge = pd.merge(person, address, on='personId', how='left')

    result=merge[['firstName', 'lastName', 'city', 'state']]


    #print(result)

    return result
    
