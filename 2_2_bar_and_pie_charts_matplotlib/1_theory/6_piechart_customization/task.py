import pandas as pd
import matplotlib.pyplot as plt

from data import preprocess, read, aggregate, filter_platforms



def plot_region(ax: plt.Axes, data: pd.DataFrame, region: str, trace: int = 0):
    ...  # TODO


def plot(games: pd.DataFrame) -> plt.Figure:
    games = aggregate(games)
    games = filter_platforms(games)

    fig, ax = plt.subplots()

    ax.pie(
        "count",
        labels="platform",
        autopct='%.2f%%',
        colors=["gray", "blue", "green", "cyan"],
        explode=[0.01, 0.01, 0.01, 0.01],
        data=games,
    )

    ax.set_title("Proportion of games per platform")
    fig.tight_layout()

    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
