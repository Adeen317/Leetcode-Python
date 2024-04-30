import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world1=world[(world['area']>=3000000) | (world['population'] >= 25000000)]
    
    return world1[['name', 'population','area']]
