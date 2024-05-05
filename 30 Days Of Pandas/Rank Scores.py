import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_df = scores.sort_values(by='score', ascending=False)
    sorted_df['rank'] = sorted_df['score'].rank(method='dense', ascending=False).astype(float)
    
    return sorted_df[['score','rank']]
    
