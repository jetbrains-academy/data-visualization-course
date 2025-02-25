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


def filter_by_publisher_and_global_sales(data: pd.DataFrame) -> pd.DataFrame:
    filtered_data = data[data["publisher"].isin(["Ubisoft", "Electronic Arts"])]
    return filtered_data[filtered_data["global_sales"] <= filtered_data["global_sales"].quantile(0.95)]
