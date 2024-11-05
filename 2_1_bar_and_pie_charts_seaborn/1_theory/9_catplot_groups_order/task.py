import pandas as pd
import seaborn as sns

from data import add_decades, extract_sales_region, preprocess, read, get_sorted_regions


def plot(games: pd.DataFrame):
    games = add_decades(games)
    games = extract_sales_region(games)

    return sns.catplot(
        data=games,
        x="decade",
        y="sales",
        estimator="sum",
        errorbar=None,
        hue="region",
        hue_order=get_sorted_regions(games),
        kind="bar",
    )


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
