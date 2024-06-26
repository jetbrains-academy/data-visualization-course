## Goal

The main goal of the lesson is to **plot the correlation between user score and critic score**.

## Theory

In seaborn there are several ways to plot relational graphs, but we will focus on two of them:

1. Using [`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html) (stands for **rel**ational **plot**).
   This function can plot both line and scatter plots.
2. Using [`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html) (stands for
   **l**inear **m**odel **plot**). This function focuses on plotting regression lines. We will talk about it a bit
   later.

For now, we will work with `relplot` function. 

Every plotting function in seaborn accepts three main arguments:

* `data` – Input data structure. In this course we will have been passing pandas dataframes here.
* `x` – Name of a column to visualize on x-axis.
* `y` – Name of a column to visualize on y-axis.

Note that `data` is optional. In this case, `x` and `y` must be lists containing some data.

Let's do some practice!

## Task

Modify the `plot` by adding a call of the `relplot` function there. Pass `games` there as a data, `user_score` for x-axis
and `critic_score` for y-axis to it.

Note that we preprocessed data for you, but if you want you can do it by yourself. Please see the corresponding hint
below.

## Hints

<div class="hint" title="How to run the code?">
TODO
</div>

<div class="hint" title="Where to find my figure?">
TODO
</div>

<div class="hint" title="How should I preprocess the data?">
TODO
</div>

<div class="hint" title="How the figure should look like?">
TODO
</div>
