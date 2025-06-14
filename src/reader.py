import pandas as pd


def read_from_csv(filename: str) -> list[dict]:
    """ читаем данные из csv формата и возвращаем список словарей """

    df = pd.read_csv(filename, delimiter=';', encoding='utf-8')
    df = df.replace(pd.NA, None)
    return df.to_dict(orient='records')


def read_from_xlcx(filename: str) -> list[dict]:
    """ читаем данные из xlcx формата и возвращаем список словарей """

    df = pd.read_excel(filename)
    df = df.replace(pd.NA, None)
    return df.head().to_dict(orient='records')
