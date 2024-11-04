import pandas as pd

from data import read


def plot(games: pd.DataFrame):
    print(games)


def main():
    games = read()
    plot(games)


if __name__ == "__main__":
    main()
