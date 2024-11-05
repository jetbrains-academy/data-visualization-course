import pandas as pd

from common.paths import GAMES_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(GAMES_DATASET_PATH)


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    data.columns = [col.lower() for col in data.columns]

    data = data[data["user_score"] != "tbd"]
    data = data.dropna()

    data["user_score"] = data["user_score"].astype("float")
    data["year_of_release"] = data["year_of_release"].astype("int")

    return data
