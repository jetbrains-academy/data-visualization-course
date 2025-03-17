import matplotlib.pyplot as plt
import pandas as pd

from data import filter_by_publisher_and_global_sales, get_bins, get_weights, preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()

    for publisher in ["Electronic Arts", "Ubisoft"]:
        publisher_df = filter_by_publisher_and_global_sales(games, publisher)
        ax.hist(
            data=publisher_df,
            x="global_sales",
            alpha=0.7,
            weights=get_weights(publisher_df),
            bins=get_bins(games),
            histtype="step",
            label=publisher,
        )

    ax.set_xlabel("Global Sales (millions)")
    ax.set_ylabel("Proportion")
    ax.set_title("Global Sales Distribution for Electronic Arts and Ubisoft")
    ax.legend()

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
