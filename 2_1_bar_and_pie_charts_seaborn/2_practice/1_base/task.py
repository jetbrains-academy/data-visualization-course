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


def main():
    votes = read()

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
