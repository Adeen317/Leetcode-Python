import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    # Filter the DataFrame to get users with valid emails
    valid_emails = users[users['mail'].str.match('^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$')]
    return valid_emails
    
