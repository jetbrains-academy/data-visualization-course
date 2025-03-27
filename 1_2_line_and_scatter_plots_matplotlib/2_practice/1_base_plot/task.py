import matplotlib.pyplot as plt
import pandas as pd

from data import read


def configure_axes(ax: plt.Axes):
    ax.set_xticks([-4, 0, 4])
    ax.set_xlabel("x")

    ax.set_yticks([-1.5, 0, 1.5])
    ax.set_ylabel("y")

    ax.spines[["right", "top"]].set_visible(False)


def add_traces(ax: plt.Axes, experiment: pd.DataFrame):
    ax.plot("x", "approximated_y", color="navy", data=experiment)
    ax.scatter("x", "y", color="grey", alpha=0.05, data=experiment)


def plot(experiment: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()

    add_traces(ax, experiment)
    configure_axes(ax)

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    experiment = read()

    fig = plot(experiment)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
