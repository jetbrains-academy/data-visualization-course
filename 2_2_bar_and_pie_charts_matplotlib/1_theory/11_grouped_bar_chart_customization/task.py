import matplotlib.pyplot as plt
import pandas as pd

from data import (
    aggregate,
    get_all_decades,
    get_number_of_decades,
    get_region_sales,
    preprocess,
    read,
)


def plot_region(ax: plt.Axes, data: pd.DataFrame, region: str, trace: int = 0):
    number_of_groups = get_number_of_decades(data)
    regions_ordered = ["other", "jp", "na", "eu"]
    group_size = len(regions_ordered) + 1
    region_sales = get_region_sales(data, region)

    ax.bar(
        [x + trace for x in range(0, number_of_groups * group_size, group_size)],
        region_sales,
        width=1,
        label=region,
    )


def plot(games: pd.DataFrame) -> plt.Figure:
    games = aggregate(games)
    regions_ordered = ["other", "jp", "na", "eu"]

    fig, ax = plt.subplots()

    for i, region in enumerate(regions_ordered):
        plot_region(ax, games, region, i)

    ax.set_xlabel("Decade")
    ax.set_ylabel("Sales")
    ax.set_title("Total sales over decades for each region")

    number_of_groups = get_number_of_decades(games)
    group_size = len(regions_ordered) + 1

    ax.set_xticks([x + 1.5 for x in range(0, number_of_groups * group_size, group_size)], get_all_decades(games))

    ax.legend()

    fig.tight_layout()

    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
