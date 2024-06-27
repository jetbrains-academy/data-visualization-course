import pandas as pd

from common import HISTOGRAM_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(HISTOGRAM_DATASET_PATH, index_col=0)
