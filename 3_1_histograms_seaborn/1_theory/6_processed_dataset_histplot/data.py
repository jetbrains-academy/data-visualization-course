import pandas as pd

from common.paths import GAMES_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(GAMES_DATASET_PATH)


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    data = data[data.User_Score != "tbd"]
    data["User_Score"] = data["User_Score"].astype("float")
    data.columns = [col.lower() for col in data.columns]
    return data.dropna()
