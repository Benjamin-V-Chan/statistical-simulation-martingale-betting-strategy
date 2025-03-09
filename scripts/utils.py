import pandas as pd

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

def load_csv(filename):
    return pd.read_csv(filename)
