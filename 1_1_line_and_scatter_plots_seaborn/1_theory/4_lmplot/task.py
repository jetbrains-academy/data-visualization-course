import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    return sns.lmplot(games, x="user_score", y="critic_score")


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
