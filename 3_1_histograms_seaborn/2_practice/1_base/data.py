import numpy as np
import pandas as pd

from common.paths import SALES_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(SALES_DATASET_PATH)


def get_bins(sales: pd.DataFrame) -> np.ndarray:
    start = (sales["sales"].min() // 100) * 100
    end = ((sales["sales"].max() // 100) + 1) * 100

    return np.array(list(range(start, end + 1, 100)))
