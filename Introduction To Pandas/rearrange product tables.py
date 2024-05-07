import pandas as pd

def rearrange_products_table(df: pd.DataFrame) -> pd.DataFrame:
    

    # Define a list of DataFrames, each representing one store
    dfs = []

    # Iterate over each store column and create a DataFrame for each
    for store in ['store1', 'store2', 'store3']:
        
        # Select rows where the price is not NULL for the current store
        store_df = df[['product_id', store]].dropna()

        # Rename the store column to 'store'
        store_df.columns = ['product_id', 'price']

        # Add the store name column
        store_df['store'] = store

        # Reorder columns to have 'store' column first
        store_df = store_df[['product_id', 'store', 'price']]

        # Add the current store DataFrame to the list
        dfs.append(store_df)

    # Concatenate the list of DataFrames along the rows (axis=0)
    result = pd.concat(dfs, ignore_index=True)

    # Display the result DataFrame
    return result



    
