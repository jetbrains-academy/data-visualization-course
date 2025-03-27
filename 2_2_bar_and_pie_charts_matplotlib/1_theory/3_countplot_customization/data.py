import pandas as pd

from common.paths import GAMES_DATASET_PATH

pd.options.mode.copy_on_write = True


def read() -> pd.DataFrame:
    return pd.read_csv(GAMES_DATASET_PATH)


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    data.columns = [col.lower() for col in data.columns]

    data = data.dropna(
        subset=[
            "platform",
            "year_of_release",
            "global_sales",
            "eu_sales",
            "jp_sales",
            "na_sales",
            "other_sales",
        ],
    )

    data["year_of_release"] = data["year_of_release"].astype("int")

    return data


def aggregate(games: pd.DataFrame) -> pd.DataFrame:
    return games["platform"].value_counts().reset_index()


def filter_platforms(data: pd.DataFrame) -> pd.DataFrame:
    return data[data["platform"].isin(["PS4", "XOne", "PC", "WiiU"])]
