import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def export_csv(df : pd.DataFrame, columns=None, filename="export.csv"):

    DATA_DIR.mkdir(exist_ok=True)
    filepath = DATA_DIR / filename

    if columns:
        columns = list(dict.fromkeys(columns))
        df[columns].to_csv(filepath, index=False)

    else:
        df.to_csv(filepath, index=False)