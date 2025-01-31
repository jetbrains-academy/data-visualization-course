import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    return sns.catplot(data=games, x="platform", kind="count")


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
