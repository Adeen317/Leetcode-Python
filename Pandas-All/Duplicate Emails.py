import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Group by 'email' and count the occurrences
    email_counts = person.groupby('email').size()

    # Filter emails that appear more than once
    duplicate_emails = email_counts[email_counts > 1].index.tolist()
    return pd.DataFrame({f"Email": [duplicate_emails]})
    
