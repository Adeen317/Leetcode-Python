import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Convert event_date to datetime
    activity['event_date'] = pd.to_datetime(activity['event_date'])

    # Group by player_id and find the minimum event_date
    result = activity.groupby('player_id')['event_date'].min().reset_index()

    # Rename columns
    result.columns = ['player_id', 'first_login']
    return result
    
