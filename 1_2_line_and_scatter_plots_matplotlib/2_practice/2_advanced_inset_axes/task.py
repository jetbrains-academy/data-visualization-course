import matplotlib.pyplot as plt
import pandas as pd

from data import read


def configure_axes(ax: plt.Axes):
    ax.set_xticks([-4, 0, 4])
    ax.set_xlim(-4, 4)
    ax.set_xlabel("x")

    ax.set_yticks([-1.5, 0, 1.5])
    ax.set_ylim(-2, 2)
    ax.set_ylabel("y")

    ax.spines[["right", "top"]].set_visible(False)


def add_traces(ax: plt.Axes, experiment: pd.DataFrame):
    ax.plot("x", "approximated_y", color="navy", data=experiment)
    ax.scatter("x", "y", color="gray", alpha=0.05, data=experiment)


def plot(experiment: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()

    inset_ax = ax.inset_axes(
        [0.15, 0.7, 0.3, 0.3],
        xlim=[0.5, 1.5],
        ylim=[0.6, 1.1],
        xticks=[0.5, 1.5],
        yticks=[0.6, 1.1],
    )

    add_traces(ax, experiment)
    add_traces(inset_ax, experiment)

    configure_axes(ax)
    ax.indicate_inset_zoom(inset_ax)

    return fig


def main():
    experiment = read()

    fig = plot(experiment)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
