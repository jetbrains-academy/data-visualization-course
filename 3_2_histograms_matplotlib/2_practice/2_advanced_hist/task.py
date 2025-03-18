import matplotlib.pyplot as plt
import pandas as pd

from data import get_bins, get_city_sales, get_median, get_weights, get_y_coordinates, read


def plot(sales: pd.DataFrame) -> plt.Figure:
    fig, (ax_ind, ax_hist) = plt.subplots(2, 1, height_ratios=[1, 10])

    color_map = {
        "Yerevan": "pink",
        "Belgrade": "grey",
    }

    edge_color_map = {
        "Yerevan": "crimson",
        "Belgrade": "black",
    }

    position_map = {
        "Yerevan": "right",
        "Belgrade": "left",
    }

    shift_map = {
        "Yerevan": -25,
        "Belgrade": 25,
    }

    for city in ["Yerevan", "Belgrade"]:
        city_sales = get_city_sales(sales, city)

        ax_hist.hist(
            x=city_sales,
            alpha=0.5,
            weights=get_weights(city_sales),
            label=city,
            bins=get_bins(sales),
            color=color_map[city],
            edgecolor=edge_color_map[city],
            histtype="step",
        )

        ax_hist.axvline(
            get_median(city_sales),
            linestyle="dashed",
            linewidth=1.5,
            label="Median",
            color=edge_color_map[city],
        )

        ax_hist.text(
            get_median(city_sales) + shift_map[city],
            0.005,
            get_median(city_sales),
            horizontalalignment=position_map[city],
            color=edge_color_map[city],
        )

        ax_ind.scatter(
            city_sales,
            get_y_coordinates(city_sales, city),
            alpha=0.1,
            label=f"{city} Observations",
            color=color_map[city],
            edgecolors=edge_color_map[city],
        )

    ax_hist.set_ylabel("Probability")
    ax_hist.set_xlabel("Sales")
    ax_hist.legend()

    handles, labels = ax_hist.get_legend_handles_labels()
    filtered_handles = [handle for handle, label in zip(handles, labels) if label != "Median"]
    filtered_labels = [label for label in labels if label != "Median"]

    ax_hist.legend(filtered_handles, filtered_labels)

    ax_ind.set_ylim(0, 0.3)
    ax_ind.spines[["top", "bottom", "left", "right"]].set_visible(False)
    ax_ind.set_xticks([])
    ax_ind.set_yticks([])

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    sales = read()

    fig = plot(sales)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
