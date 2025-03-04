import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data import filter_by_publisher_and_global_sales, get_max_sales, get_min_sales, preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    publishers = ["Electronic Arts", "Ubisoft"]

    min, max = get_min_sales(games), get_max_sales(games)
    bins = np.linspace(min, max, num=11)

    for publisher in publishers:
        publisher_df = filter_by_publisher_and_global_sales(games, publisher)
        weights = np.ones_like(publisher_df["global_sales"]) / publisher_df["global_sales"].shape[0]
        ax.hist(data=publisher_df, x="global_sales", alpha=0.7, weights=weights, bins=bins, histtype="step")

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("example.png", dpi=300)


if __name__ == "__main__":
    main()
