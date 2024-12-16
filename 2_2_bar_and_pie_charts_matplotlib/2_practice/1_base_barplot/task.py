import matplotlib.pyplot as plt
import pandas as pd

from data import get_categories_sorted, get_category_products, get_category_size, get_category_votes, read


def plot_region(ax: plt.Axes, data: pd.DataFrame, category: str, color: str, trace: int = 0):
    category_votes = get_category_votes(data, category)
    category_size = get_category_size(data, category)

    ax.barh(
        [x + trace for x in range(category_size)],
        category_votes,
        color=color,
    )


def plot(votes: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    categories_sorted = get_categories_sorted()

    colors = {
        "salad": "green",
        "cheese": "firebrick",
        "bread": "navy",
    }

    all_y_coordinates = []
    all_labels = []

    for i, category in enumerate(categories_sorted):
        category_size = get_category_size(votes, category)
        plot_region(ax, votes, category, colors[category], i * category_size)

        all_labels.extend(get_category_products(votes, category))
        all_y_coordinates.extend([i * category_size + x for x in range(category_size)])

    ax.set_xticks([])
    ax.set_title("Respondents, %")
    ax.set_xlabel("Respondents, %")
    ax.set_xlim(0, 100)
    ax.set_yticks(all_y_coordinates)
    ax.set_yticklabels(all_labels)

    return fig


def main():
    votes = read()

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
