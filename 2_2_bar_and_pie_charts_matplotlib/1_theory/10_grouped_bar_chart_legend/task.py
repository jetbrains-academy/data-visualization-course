import matplotlib.pyplot as plt
import pandas as pd

from data import (
    aggregate,
    get_all_regions,
    get_number_of_decades,
    get_number_of_regions,
    get_region_sales,
    preprocess,
    read,
)


def plot_region(ax: plt.Axes, data: pd.DataFrame, region: str, trace: int = 0):
    number_of_groups = get_number_of_decades(data)
    group_size = get_number_of_regions(data) + 1

    region_sales = get_region_sales(data, region)

    ax.bar(
        [x + trace for x in range(0, number_of_groups * group_size, group_size)],
        region_sales,
        width=1,
        label=region,
    )


def plot(games: pd.DataFrame) -> plt.Figure:
    games = aggregate(games)

    fig, ax = plt.subplots()

    for i, region in enumerate(get_all_regions(games)):
        plot_region(ax, games, region, i)

    ax.legend()

    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
