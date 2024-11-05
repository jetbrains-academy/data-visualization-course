import pandas as pd
import seaborn as sns

from data import get_sorted_platforms, preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    return sns.catplot(
        data=games,
        y="platform",
        stat="percent",
        order=get_sorted_platforms(games),
        kind="count",
    )


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
