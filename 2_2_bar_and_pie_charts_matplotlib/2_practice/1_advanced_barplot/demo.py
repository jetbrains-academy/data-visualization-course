import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import pandas as pd

from data import read


def plot(df: pd.DataFrame):
    fig, axs = plt.subplots(3, 1, figsize=(6, 6))

    # fig.subplots_adjust(hspace=0)

    color_mapping = {
        "cheese": "firebrick",
        "bread": "navy",
        "salad": "green",
    }

    for i, (group, data) in enumerate(df.groupby("food")):
        ax: plt.Axes = axs[i]
        bars = ax.barh(
            data.value,
            data.proportion,
            facecolor=color_mapping[group],
            edgecolor="black",
            linewidth=2,
        )
        ax.set_xticks([])

        for index, value in enumerate(data.proportion):
            ax.text(value + 2, index, f"{round(value, 1)}", weight="bold")

        ax.tick_params(axis="y", length=0)
        ax.tick_params(axis="x", length=6, width=2)
        ax.set_xlim(0, 100)

        ax.text(
            1.03,
            0.5,
            group.capitalize(),
            transform=ax.transAxes,
            rotation=-90,
            weight="bold",
            fontsize=16,
            verticalalignment="center",
            color=color_mapping[group],
        )

        for label in ax.get_yticklabels():
            label.set_weight("bold")

        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(2)

        # Get bar coordinates and dimension
        bars_info = [(bar.get_y() - 0.11, bar.get_width()) for bar in bars]  # TODO: improve

        for bar_y, _ in bars_info:
            ax.axhline(y=bar_y + 1, color="k", ls=(0, (5, 5)), lw=1)

    ax = axs[0]
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.xaxis.set_minor_locator(AutoMinorLocator())

    position_params = {"top": True, "labeltop": True, "bottom": False, "labelbottom": False}
    ax.tick_params(which="minor", **position_params, axis="x", length=8, width=2)
    ax.tick_params(**position_params, axis="x", length=16, width=2)

    ax.set_xlabel("Respondents, %", weight="bold", fontsize=16, labelpad=15)
    ax.xaxis.set_label_position("top")
    for label in ax.get_xticklabels():
        label.set_weight("bold")

    ax = axs[-1]
    ax.set_xticks([0, 25, 50, 75, 100])

    position_params = {"top": False, "labeltop": False, "bottom": True, "labelbottom": True}
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="minor", **position_params, axis="x", length=8, width=2)
    ax.tick_params(**position_params, axis="x", length=16, width=2)

    ax.set_xlabel("Respondents, %", weight="bold", fontsize=16, labelpad=15)
    ax.xaxis.set_label_position("bottom")
    for label in ax.get_xticklabels():
        label.set_weight("bold")

    fig.tight_layout()
    fig.show()


def main():
    games = read()
    plot(games)


if __name__ == "__main__":
    main()
