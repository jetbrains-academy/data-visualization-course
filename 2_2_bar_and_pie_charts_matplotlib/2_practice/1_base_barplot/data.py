import pandas as pd

from common.paths import FOOD_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(FOOD_DATASET_PATH)


def get_category_votes(data: pd.DataFrame, category: str) -> pd.Series:
    return data[data["category"] == category]["votes"]


def get_category_product_names(data: pd.DataFrame, category: str) -> pd.DataFrame:
    return data[data["category"] == category]["name"]


def get_category_size(data: pd.DataFrame, category: str) -> int:
    return len(data[data["category"] == category])


def get_categories(data: pd.DataFrame) -> list:
    return list(data["category"].unique())
