import pandas as pd

def exchange_seats(df: pd.DataFrame) -> pd.DataFrame:
    for i in range(0, len(df) - 1, 2):
        df.loc[i, 'id'], df.loc[i + 1, 'id'] = df.loc[i + 1, 'id'], df.loc[i, 'id']

    # Ensure the DataFrame is sorted by id in ascending order
    df = df.sort_values('id').reset_index(drop=True)
    return df
