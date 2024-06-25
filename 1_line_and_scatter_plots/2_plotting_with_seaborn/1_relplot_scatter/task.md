## Goal

The main goal of the lesson is to **plot the correlation between the user score and the critic score**.

## Theory

In seaborn, there are several ways to plot relational graphs, but we will focus on two of them:

1. Using [`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html) (stands for **rel**ational **plot**).
   This function can plot both line and scatter plots.
2. Using [`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html) (stands for
   **l**inear **m**odel **plot**). This function focuses on plotting regression lines. We will talk about it a bit
   later.

For now, we will work with the `relplot` function.

Every plotting function in seaborn accepts three main arguments:

* `data` – Input data structure. In this course, we will pass pandas dataframes here.
* `x` – Name of a column to visualize on x-axis.
* `y` – Name of a column to visualize on y-axis.

Note that `data` is optional. In this case, `x` and `y` must be lists containing some data.

The common way to import seaborn looks like this: `import seaborn as sns`.
We did it for you, so to call `relplot` you need to write `sns.relplot`.

Let's do some practice!

## Task

Modify the `plot` by adding a call of the `relplot` function there.
Pass `games` there as data, `user_score` as x-axis, and `critic_score` as y-axis to it.

Note that we preprocessed the data for you, but if you want, you can do this by yourself.
Please see the corresponding hint below.

## Hints

<div class="hint" title="How to run the code?">
To run the code, you should click on the green triangle next to the entry point. In case of execution errors,
they will be shown in the console inside the IDE. 
<img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="Where to find my figure?">
TODO
</div>

<div class="hint" title="How should I preprocess the data?">
Before using the data, we need to make several preprocessing steps:
<ol>
   <li>Lower column names.</li>
   <li>Remove games with user scores to be decided (the user score is equal to <code>tbd</code>).</li>
   <li>Drop all nans.</li>
   <li>Convert the <code>user_score</code> column to float.</li>
</ol>

If you have some difficulties with your own preprocessing, you can
have [a sneak to the inner file](file://1_line_and_scatter_plots/2_plotting_with_seaborn/1_relplot_scatter/data.py)
where our preprocessing is defined.
</div>

<div class="hint" title="How the figure should look like?">
<img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>
