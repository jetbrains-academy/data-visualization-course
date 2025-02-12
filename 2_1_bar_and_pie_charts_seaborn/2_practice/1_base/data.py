from typing import List

import pandas as pd

from common.paths import FOOD_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(FOOD_DATASET_PATH)


def get_product_order(data: pd.DataFrame) -> List:
    return (
        data.drop_duplicates(subset=["category", "product"])
        .sort_values(
            by=["category", "product"],
            ascending=[True, False],
        )["product"]
        .to_list()
    )
