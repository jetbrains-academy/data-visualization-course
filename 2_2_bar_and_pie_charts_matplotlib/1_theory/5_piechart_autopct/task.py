import pandas as pd
import matplotlib.pyplot as plt

from data import preprocess, read, aggregate, filter_platforms


def plot_region(ax: plt.Axes, data: pd.DataFrame, region: str, trace: int = 0):
    ...  # TODO: do not implement this function until the corresponding task


def plot(games: pd.DataFrame) -> plt.Figure:
    games = aggregate(games)
    games = filter_platforms(games)

    fig, ax = plt.subplots()

    ax.pie("count", labels="platform", autopct="%.2f%%", data=games)

    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
