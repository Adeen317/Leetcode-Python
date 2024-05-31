import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    a = followers.groupby('user_id').size().reset_index(name='followers_count')
    b = a.sort_values(by='user_id').reset_index(drop=True)
    return pd.DataFrame(b)
    
