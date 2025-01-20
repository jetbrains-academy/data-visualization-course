import pandas as pd
import seaborn as sns

from data import get_product_order, read


def plot(votes: pd.DataFrame) -> sns.FacetGrid:
    return sns.catplot(
        votes,
        y="product",
        hue="category",
        order=get_product_order(votes),
        kind="count",
    )


# Please solve the task in the plot function and do not modify this one
def main():
    votes = read()

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
