import pandas as pd


def read_from_csv(filename: str) -> list[dict]:
    df = pd.read_csv(filename, delimiter=';', encoding='utf-8', na_values=['NA', 'NaN'])
    df = df.replace(pd.NA, None)
    return df.to_dict(orient='records')
