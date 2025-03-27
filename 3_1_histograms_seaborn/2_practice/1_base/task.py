import pandas as pd
import seaborn as sns

from data import get_bins, read


def plot(sales: pd.DataFrame) -> sns.FacetGrid:
    return sns.displot(sales, x="sales", hue="city", stat="probability", common_norm=False, bins=get_bins(sales))


# Please solve the task in the plot function and do not modify this one
def main():
    sales = read()

    fig = plot(sales)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
