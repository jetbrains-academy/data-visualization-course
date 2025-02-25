import pandas as pd
import seaborn as sns

from data import filter_by_global_sales, preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    return sns.displot(data=filter_by_global_sales(games), x="global_sales", bins=10)


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
