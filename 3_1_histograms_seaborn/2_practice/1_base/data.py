import pandas as pd

from common.paths import SALES_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(SALES_DATASET_PATH)


def get_bins(sales: pd.DataFrame) -> list:
    start = (sales["sales"].min() // 100) * 100
    end = ((sales["sales"].max() // 100) + 1) * 100

    return list(range(start, end + 1, 100))
