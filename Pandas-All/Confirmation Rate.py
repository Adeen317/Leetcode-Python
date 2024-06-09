import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    
    a=pd.merge(signups,confirmations,how='left',on='user_id').fillna(0)
    confirmation=a.groupby('user_id').agg(total_requests=('user_id', 'size'), confirmed_requests=('action', lambda x: (x == 'confirmed').sum())
).reset_index()

    confirmation['confirmation_rate'] = (confirmation['confirmed_requests'] / confirmation['total_requests']).fillna(0).round(2)

    final_result = confirmation[['user_id', 'confirmation_rate']].sort_values(by='user_id').reset_index(drop=True)

    return pd.DataFrame(final_result)
