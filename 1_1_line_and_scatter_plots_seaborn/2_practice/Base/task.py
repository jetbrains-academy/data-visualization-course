import pandas as pd
import seaborn as sns

from data import read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    return sns.lmplot(
        x="x",
        y="y",
        data=games,
        scatter_kws={"color": "grey", "alpha": 0.05},
        line_kws={"color": "navy"},
    )


def main():
    games = read()

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
