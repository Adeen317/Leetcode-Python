#602
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    combined_ids = pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']])

    # Group by id and count occurrences
    id_counts = combined_ids.value_counts().reset_index()
    id_counts.columns = ['id', 'num']

    result = id_counts.sort_values(by='num', ascending=False).head(1)
    
    return result
    
