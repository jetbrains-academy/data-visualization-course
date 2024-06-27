import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame):
    sns.histplot(data=games, x="global_sales")


def main():
    games = read()
    games = preprocess(games)

    plot(games)
    plt.show()


if __name__ == "__main__":
    main()
