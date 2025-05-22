import pandas as pd
import seaborn as sns

from data import filter_by_global_sales, filter_by_publisher, preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    filtered_games = filter_by_publisher(games)
    filtered_games = filter_by_global_sales(filtered_games)

    return sns.displot(
        data=filtered_games,
        x="global_sales",
        bins=10,
        hue="publisher",
        stat="probability",
    )


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
