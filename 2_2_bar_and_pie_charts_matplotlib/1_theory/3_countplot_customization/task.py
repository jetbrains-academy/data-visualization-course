import matplotlib.pyplot as plt
import pandas as pd

from data import aggregate, filter_platforms, preprocess, read


def plot_region(ax: plt.Axes, games: pd.DataFrame, region: str, trace: int = 0):
    # TODO: do not implement this function until the corresponding task
    pass


def plot(games: pd.DataFrame) -> plt.Figure:
    games = aggregate(games)
    games = filter_platforms(games)

    fig, ax = plt.subplots()
    ax.barh("platform", "count", color=["gray", "blue", "green", "cyan"], data=games)

    ax.set_xlabel("Count")
    ax.set_ylabel("Platform")
    ax.set_title("Number of games per platform")

    fig.tight_layout()

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
