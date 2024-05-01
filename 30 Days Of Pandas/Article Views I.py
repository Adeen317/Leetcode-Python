import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    view = views[(views['author_id']==views['viewer_id'])]
    view=view.sort_values(by='author_id')
    view=view.drop_duplicates(subset='author_id', keep= 'first')
    view=view.rename(columns={'viewer_id': 'id'})
    return view[['id']]
