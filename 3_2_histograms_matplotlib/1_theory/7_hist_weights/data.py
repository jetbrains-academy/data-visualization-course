import numpy as np
import pandas as pd

from common.paths import GAMES_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(GAMES_DATASET_PATH)


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    data.columns = [col.lower() for col in data.columns]

    data = data[data["user_score"] != "tbd"]
    data = data.dropna(
        subset=[
            "platform",
            "critic_score",
            "user_score",
            "global_sales",
            "eu_sales",
            "jp_sales",
            "na_sales",
            "other_sales",
        ],
    )

    data["user_score"] = data["user_score"].astype("float")

    return data


def filter_by_global_sales(data: pd.DataFrame) -> pd.DataFrame:
    return data[data["global_sales"] <= data["global_sales"].quantile(0.95)]


def filter_by_publisher(data: pd.DataFrame, publisher: str) -> pd.DataFrame:
    return data[data["publisher"] == publisher]


def get_weights(data: pd.DataFrame) -> np.ndarray:
    return np.ones_like(data["global_sales"]) / data["global_sales"].shape[0]
