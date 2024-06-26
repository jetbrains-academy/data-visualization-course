import pandas as pd

from common import EXPERIMENT_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(EXPERIMENT_DATASET_PATH, index_col=0)
