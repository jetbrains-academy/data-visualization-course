import matplotlib.pyplot as plt
import pandas as pd

from data import get_categories, get_category_product_names, get_category_size, get_category_votes, preprocess, read


def plot_category(ax: plt.Axes, votes: pd.DataFrame, category: str, color: str, offset: int = 0):
    category_votes = get_category_votes(votes, category)
    category_size = get_category_size(votes, category)

    positions = [x + offset for x in range(category_size)]

    ax.barh(
        positions,
        category_votes,
        color=color,
        label=category,
    )

    for position, vote in zip(positions, category_votes):
        ax.text(vote + 1, position, f"{round(vote, 1)}", verticalalignment="center")


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
    for category in get_categories(votes):
        category_size = get_category_size(votes, category)

        plot_category(ax, votes, category, colors[category], offset)

        positions = [x + offset for x in range(category_size)]

        y_tick_labels.extend(get_category_product_names(votes, category))
        y_tick_coordinates.extend(positions)

        offset += category_size

    ax.set_yticks(y_tick_coordinates, y_tick_labels)
    ax.set_ylabel("Product name")

    ax.get_xticks()

    ax.set_xlim(0, 100)
    ax.set_xticks(range(0, 101, 25))
    ax.set_xticks(range(0, 101, 5), minor=True)
    ax.set_xlabel("Respondents, %")
    ax.tick_params(top=True, labeltop=True, axis="x", which="both")

    ax.set_title("Distribution of votes per category")

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(reversed(handles), reversed(labels))

    fig.tight_layout()

    return fig


def main():
    votes = read()
    votes = preprocess(votes)

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
