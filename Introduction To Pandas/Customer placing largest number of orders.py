import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if len(orders) < 1:
        return pd.DataFrame({f"customer_number": [None]})
        
    order=orders.sort_values(by='order_number',ascending=False)
    customer = order['customer_number'].unique()
    
    if len('customer') >= 1:
        return pd.DataFrame({f"customer_number": [customer[0]]})
    
    else:
        return pd.DataFrame({f"customer_number": [None]})
