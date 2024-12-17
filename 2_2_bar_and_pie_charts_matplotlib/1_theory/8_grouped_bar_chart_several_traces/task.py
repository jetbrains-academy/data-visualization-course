import matplotlib.pyplot as plt
import pandas as pd

from data import aggregate, get_all_regions, get_number_of_decades, get_region_sales, preprocess, read


def plot_region(ax: plt.Axes, data: pd.DataFrame, region: str, trace: int = 0):
    number_of_groups = get_number_of_decades(data)
    region_sales = get_region_sales(data, region)

    ax.bar(range(number_of_groups), region_sales)


def plot(games: pd.DataFrame) -> plt.Figure:
    games = aggregate(games)

    fig, ax = plt.subplots()

    for region in get_all_regions(games):
        plot_region(ax, games, region)

    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
