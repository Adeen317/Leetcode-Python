import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animal=animals.sort_values(by='weight',ascending=False, inplace=True)
    a=animals[animals['weight'] >= 100]
    return pd.DataFrame(a['name'])
