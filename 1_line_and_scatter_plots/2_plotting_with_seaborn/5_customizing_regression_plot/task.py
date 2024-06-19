import pandas as pd
import seaborn as sns

from data import read, preprocess


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    return sns.lmplot(
        games,
        x='user_score',
        y='critic_score',
        line_kws={'color': 'firebrick'},
        scatter_kws={'alpha': 0.1},
    )


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == '__main__':
    main()
