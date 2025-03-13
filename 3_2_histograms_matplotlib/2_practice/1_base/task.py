import matplotlib.pyplot as plt
import pandas as pd

from data import get_bins, get_city_sales, get_weights, read


def plot(sales: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()

    line_color_map = {
        "Yerevan": "pink",
        "Belgrade": "grey",
    }

    edge_color_map = {
        "Yerevan": "crimson",
        "Belgrade": "black",
    }

    for city in ["Yerevan", "Belgrade"]:
        city_sales = get_city_sales(sales, city)
        weights = get_weights(city_sales)

        ax.hist(
            x=city_sales,
            alpha=0.5,
            weights=weights,
            label=city,
            bins=get_bins(sales),
            color=line_color_map[city],
            edgecolor=edge_color_map[city],
            histtype="step",
        )

    ax.set_ylabel("Probability")
    ax.set_xlabel("Sales")
    ax.legend()

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    sales = read()

    fig = plot(sales)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
