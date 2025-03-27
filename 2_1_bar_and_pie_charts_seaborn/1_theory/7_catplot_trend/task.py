import pandas as pd
import seaborn as sns

from data import add_decades, preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    games = add_decades(games)

    return sns.catplot(
        data=games,
        x="decade",
        y="global_sales",
        estimator="sum",
        errorbar=None,
        kind="bar",
    )


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
