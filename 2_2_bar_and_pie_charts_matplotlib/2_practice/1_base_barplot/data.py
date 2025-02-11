from typing import List

import pandas as pd

from common.paths import FOOD_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(FOOD_DATASET_PATH)


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    preprocessed_data = data.groupby(["category", "product"]).count() / data["participant"].nunique() * 100
    preprocessed_data = preprocessed_data.rename(columns={"participant": "votes"})
    return preprocessed_data.reset_index()


def get_category_votes(data: pd.DataFrame, category: str) -> pd.Series:
    return data[data["category"] == category].sort_values(by="product")["votes"]


def get_category_product_names(data: pd.DataFrame, category: str) -> pd.DataFrame:
    return data[data["category"] == category]["product"].sort_values(ascending=True)


def get_category_size(data: pd.DataFrame, category: str) -> int:
    return len(data[data["category"] == category])


def get_categories(data: pd.DataFrame) -> List:
    return list(data["category"].unique())
