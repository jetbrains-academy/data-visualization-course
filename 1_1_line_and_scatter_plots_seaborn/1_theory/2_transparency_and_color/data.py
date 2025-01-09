import pandas as pd

from common.paths import GAMES_DATASET_PATH

pd.options.mode.copy_on_write = True


def read() -> pd.DataFrame:
    return pd.read_csv(GAMES_DATASET_PATH)


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    data.columns = [col.lower() for col in data.columns]

    data = data[data["user_score"] != "tbd"]
    data = data.dropna(subset=["critic_score", "user_score"])

    data["user_score"] = data["user_score"].astype("float")

    return data
