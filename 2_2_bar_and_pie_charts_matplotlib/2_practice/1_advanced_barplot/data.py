import pandas as pd

from common.paths import FOOD_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(FOOD_DATASET_PATH, index_col=0)
