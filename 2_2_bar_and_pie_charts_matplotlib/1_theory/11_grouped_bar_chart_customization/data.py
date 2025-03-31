import numpy as np
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


def __add_decades(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    decade_bins = (
        np.array(range(data["year_of_release"].min() // 10 * 10, data["year_of_release"].max() // 10 * 10 + 11, 10)) - 1
    )

    # Dropping the last decade because of incomplete sales data
    decade_bins = decade_bins[:-1]
    decade_labels = np.array(decade_bins[:-1]) + 1

    data["decade"] = pd.cut(data["year_of_release"], bins=decade_bins, labels=decade_labels, right=True)
    return data[data["decade"].notna()]


def __extract_sales_region(data: pd.DataFrame) -> pd.DataFrame:
    sales_columns = {"eu_sales", "jp_sales", "na_sales", "other_sales"}
    other_columns = set(data.columns.unique()).difference(sales_columns)

    data = data.melt(id_vars=other_columns, value_vars=sales_columns, value_name="sales", var_name="region")
    data["region"] = data["region"].str.replace("_sales", "")

    return data


def aggregate(games: pd.DataFrame) -> pd.DataFrame:
    games = __add_decades(games)
    games = __extract_sales_region(games)
    return games.groupby(["decade", "region"], observed=True)["sales"].sum().reset_index()


def get_number_of_decades(data: pd.DataFrame) -> int:
    return data["decade"].nunique()


def get_number_of_regions(data: pd.DataFrame) -> int:
    return data["region"].nunique()


def get_region_sales(data: pd.DataFrame, region: str) -> pd.Series:
    return data[data["region"] == region]["sales"]


def get_all_regions(data: pd.DataFrame) -> list[str]:
    return data.groupby("region")["sales"].sum().sort_values(ascending=False).index.tolist()


def get_all_decades(data: pd.DataFrame) -> list[int]:
    return list(data["decade"].unique())
