import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame):
    col1, col2 = "user_score", "critic_score"
    sns.jointplot(
        data=games,
        x=col1,
        y=col2,
        kind="reg",
        joint_kws={
            "scatter_kws": {"alpha": 0.1},
            "line_kws": {"color": "firebrick"},
        },
    )


def main():
    games = read()
    games = preprocess(games)

    plot(games)
    plt.show()


if __name__ == "__main__":
    main()
