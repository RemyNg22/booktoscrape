def reset_index_liste(df):
    df = df.reset_index(drop=True)
    df.index = df.index + 1
    return df