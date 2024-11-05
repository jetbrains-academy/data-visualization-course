import numpy as np
import pandas as pd

from common.paths import GAMES_DATASET_PATH

pd.options.mode.copy_on_write = True


def read() -> pd.DataFrame:
    return pd.read_csv(GAMES_DATASET_PATH)


def add_decades(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    decade_bins = (
        np.array(range(data["year_of_release"].min() // 10 * 10, data["year_of_release"].max() // 10 * 10 + 11, 10)) - 1
    )

    # Dropping the last decade because of incomplete sales data
    decade_bins = decade_bins[:-1]
    decade_labels = np.array(decade_bins[:-1]) + 1

    data["decade"] = pd.cut(data["year_of_release"], bins=decade_bins, labels=decade_labels, right=True)
    return data[data["decade"].notna()]


def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    data.columns = [col.lower() for col in data.columns]

    data = data.dropna(
        subset=[
            "platform",
            "year_of_release",
            "global_sales",
            "eu_sales",
            "jp_sales",
            "na_sales",
            "other_sales",
        ],
    )

    data["year_of_release"] = data["year_of_release"].astype("int")

    return data
