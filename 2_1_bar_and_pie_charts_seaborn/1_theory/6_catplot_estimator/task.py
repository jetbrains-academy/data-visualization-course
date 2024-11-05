import pandas as pd
import seaborn as sns

from data import preprocess, read, filter_platforms, get_sorted_platforms


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    games = filter_platforms(games)

    return sns.catplot(
        data=games,
        x="platform",
        y="global_sales",
        estimator="median",
        errorbar=None,
        order=get_sorted_platforms(games),
        kind="bar",
    )


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
