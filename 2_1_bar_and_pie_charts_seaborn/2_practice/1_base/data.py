import pandas as pd

from common.paths import FOOD_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(FOOD_DATASET_PATH)


def get_product_order(data: pd.DataFrame) -> list:
    return (
        data.drop_duplicates(subset=["category", "product"])
        .groupby("category", sort=False)
        .apply(lambda group: group["product"].sort_values(), include_groups=False)
        .to_list()
    )
