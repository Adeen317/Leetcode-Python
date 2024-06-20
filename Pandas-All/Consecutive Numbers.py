import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev_num'] = logs['num'].shift(1)
    logs['next_num'] = logs['num'].shift(-1)
    logs['prev_id'] = logs['id'].shift(1)
    logs['next_id'] = logs['id'].shift(-1)
    
    # Filter based on the conditions
    condition = (
        (logs['num'] == logs['prev_num']) & 
        (logs['num'] == logs['next_num']) & 
        (logs['id'] == logs['prev_id'] + 1) & 
        (logs['id'] == logs['next_id'] - 1)
    )
    
    # Select distinct num values that meet the condition
    result = logs.loc[condition, 'num'].unique()
    
    # Convert to DataFrame and return
    return pd.DataFrame(result, columns=['ConsecutiveNums'])
