from typing import List

import numpy as np
import pandas as pd

from common.paths import SALES_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(SALES_DATASET_PATH)


def get_city_sales(sales: pd.DataFrame, city: str) -> pd.Series:
    return sales[sales["city"] == city]["sales"]


def get_weights(sales: pd.Series) -> np.ndarray:
    return np.ones_like(sales) / sales.shape[0]


def get_bins(sales: pd.DataFrame) -> List:
    start = (sales["sales"].min() // 100) * 100
    end = ((sales["sales"].max() // 100) + 1) * 100

    return list(range(start, end + 1, 100))


def get_median(sales: pd.Series) -> float:
    return sales.median()


def get_y_coordinates(sales: pd.Series, city: str) -> List[float]:
    if city == "Belgrade":
        return [0.2] * len(sales)
    if city == "Yerevan":
        return [0.1] * len(sales)

    error_message = f"Unknown city: {city}"
    raise ValueError(error_message)
