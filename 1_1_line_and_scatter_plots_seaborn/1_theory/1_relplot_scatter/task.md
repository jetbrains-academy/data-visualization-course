## Goal

The main goal of the lesson is to **plot the correlation between user scores and critic scores**.

## Theory

In Seaborn, there are several ways to plot relational graphs, but we will focus on two of them:

1. [`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html) (stands for **rel**ational **plot**):
   This function can plot both line and scatter plots.
2. [`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html) (stands for **l**inear **m**odel **plot**):
   This function focuses on plotting regression lines.
   We will talk about it a bit later.

For now, we will work with the `relplot` function.

Every plotting function in Seaborn accepts three main arguments:

* `data`: The input data structure (for example, Pandas DataFrame or some mapping).
* `x`: The name of the column to visualize on the x-axis.
* `y`: The name of the column to visualize on the y-axis.

Note that the `data` argument is optional.
If you do not provide it, `x` and `y` must be collections containing the data to plot.

While using Seaborn, we recommend passing `data` as a positional argument
and any other arguments (including `x` and `y`) as keyword arguments.
For example: `sns.relplot(my_data, x="column_x", y="column_y", some_argument="some_value")`.

The common way to import Seaborn is as follows: `import seaborn as sns`.
We've already done this for you, so to call `relplot`, you simply need to write `sns.relplot`.

Now, let's do some practice!

## Task

Modify the `plot` by adding a call to the `relplot` function.
Pass `games` there as the data, `user_score` as the x-axis, and `critic_score` as the y-axis.

Note that we preprocessed the data for you, but if you prefer, you can do this yourself.
Please see the corresponding hint below.

## Hints

<div class="hint" title="How to run the code?">
   To run the code, click the green triangle next to the entry point.
   In case of execution errors, they will be displayed in the console inside the IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="Where to find my figure?">
   After running the code, the graph will be generated next to the <code>task.py</code> file.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="How should I preprocess the data?">
   Before using the data, we need to perform several preprocessing steps:
   <ol>
      <li>Convert column names to lowercase.</li>
      <li>Remove games with undecided user scores (where the user score is equal to <code>tbd</code>).</li>
      <li>Drop all NaN values from the following columns:</li>
      <ul>
         <li><code>critic_score</code></li>
         <li><code>user_score</code></li>
      </ul>
      <li>Convert the <code>user_score</code> column to a float.</li>
   </ol>
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
