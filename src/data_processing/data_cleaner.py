import pandas as pd

def clean_data(df: pd.DataFrame):
    # Удаление дубликатов
    df = df.drop_duplicates()
    # Заполнение пропусков
    df = df.ffill().bfill()
    return df