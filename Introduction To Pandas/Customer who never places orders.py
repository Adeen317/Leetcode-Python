import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')

    # Filter out customers who haven't placed any orders
    customers_sec = merged_df[merged_df['id_y'].isnull()]['name']
    

    return pd.DataFrame({f"Customers": [customers_sec]})
    
