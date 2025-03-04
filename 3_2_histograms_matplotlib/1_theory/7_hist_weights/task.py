import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data import filter_by_publisher_and_global_sales, preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    publishers = ["Electronic Arts", "Ubisoft"]

    for publisher in publishers:
        publisher_df = filter_by_publisher_and_global_sales(games, publisher)
        weights = np.ones_like(publisher_df["global_sales"]) / publisher_df["global_sales"].shape[0]
        ax.hist(data=publisher_df, x="global_sales", alpha=0.7, weights=weights)

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
