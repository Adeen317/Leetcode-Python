import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_company = company[company['name'] == 'RED']
    if not red_company.empty:
        red_com = red_company['com_id'].values[0]

        sales_ids = orders[orders['com_id'] == red_com]['sales_id'].unique()

        result = sales_person[~sales_person['sales_id'].isin(sales_ids)][['name']]

    else:
        result = sales_person[['name']]

    return result
    
