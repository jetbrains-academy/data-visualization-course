import matplotlib.pyplot as plt
import pandas as pd

from data import get_categories, get_category_product_names, get_category_size, get_category_votes, preprocess, read


def plot_category(ax: plt.Axes, votes: pd.DataFrame, category: str, color: str, offset: int = 0):
    category_votes = list(reversed(get_category_votes(votes, category)))
    category_size = get_category_size(votes, category)

    ax.barh(
        [x + offset for x in range(category_size)],
        category_votes,
        color=color,
        label=category,
    )


def plot(votes: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()

    colors = {
        "bread": "sienna",
        "cheese": "goldenrod",
        "salad": "forestgreen",
    }

    y_tick_coordinates = []
    y_tick_labels = []

    offset = 0
    for category in reversed(get_categories(votes)):
        category_size = get_category_size(votes, category)

        plot_category(ax, votes, category, colors[category], offset)

        y_tick_labels.extend(reversed(get_category_product_names(votes, category)))
        y_tick_coordinates.extend([x + offset for x in range(category_size)])

        offset += category_size

    ax.set_yticks(y_tick_coordinates, y_tick_labels)
    ax.set_ylabel("Product name")

    ax.set_xticks(range(0, 101, 25))
    ax.set_xlabel("Respondents, %")

    ax.set_title("Distribution of votes per category")
    ax.legend()

    fig.tight_layout()

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    votes = read()
    votes = preprocess(votes)

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
