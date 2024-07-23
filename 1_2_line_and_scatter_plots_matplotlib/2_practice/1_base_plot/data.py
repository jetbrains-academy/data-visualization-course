import pandas as pd

from common.paths import EXPERIMENT_DATASET_PATH


def read() -> pd.DataFrame:
    return pd.read_csv(EXPERIMENT_DATASET_PATH)
