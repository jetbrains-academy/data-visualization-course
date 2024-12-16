import pandas as pd

from common.paths import FOOD_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(FOOD_DATASET_PATH, index_col=0)


def get_category_votes(data: pd.DataFrame, category: str) -> pd.Series:
    return data[data["food"] == category]["proportion"]


def get_category_products(data: pd.DataFrame, category: str) -> pd.DataFrame:
    return data[data["food"] == category]["value"]


def get_category_size(data: pd.DataFrame, category: str) -> int:
    return data[data["food"] == category].shape[0]


def get_categories_sorted() -> list:
    return ["salad", "cheese", "bread"]
