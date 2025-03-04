import numpy as np
import pandas as pd

from common.paths import GAMES_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(GAMES_DATASET_PATH)


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
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


def get_logarithmic_bins(data: pd.DataFrame, num: int) -> np.ndarray:
    return np.logspace(np.log10(data["global_sales"].min()), np.log10(data["global_sales"].max()), num + 1)
