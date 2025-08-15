## Goal

The main goal of the lesson is to **plot the correlation between user scores and critic scores**.

## Theory

In Matplotlib, there are several ways to plot relational graphs, but we will focus on two of them:

1. Using [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).
   This function creates scatter plots.
2. Using [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html).
   This function creates line plots.

For now, we will work with the `scatter` function.

Every plotting function in Matplotlib accepts three main arguments:

* `data`: The input data structure. (for example, Pandas DataFrame or some mapping).
* `x`: The name of the column to visualize on the x-axis.
* `y`: The name of the column to visualize on the y-axis.

There are a few important things to note:

1. `data` is optional. If we do not provide it, `x` and `y` must be collections containing data.
2. We can only specify the `data` parameter as a keyword argument.
3. We must specify the `x` and `y` parameters as positional arguments.

While using Matplotlib, we recommend passing any other arguments as keyword arguments.
For example: `plt.scatter("column_x", "column_y", data=my_data, some_argument="some_value")`.

<hr>

To start building plots with Matplotlib, you need
to create a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html) object and
at least one [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes) object.
We can think of the `Figure` as a container for several `Axes`, where the actual plotting is done.

To create a `Figure` and a single `Axes`, we can use
the [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
function: `fig, ax = plt.subplots()`.
Here, we use the common abbreviations for `Figure` (`fig`) and `Axes` (`ax`).
We are also using the common alias for Matplotlib (`plt`),
which we defined during import: `import matplotlib.pyplot as plt`.

Be aware of the difference between `Axes` and [`Axis`](https://matplotlib.org/stable/api/axis_api.html#axis-objects):
an `Axes` object can contain several `Axis` objects (usually the x-axis and y-axis).

As we mentioned earlier, the actual plotting is done within the `Axes`. 
To plot something in the figure, we should call methods from the `Axes` instance.
For example, to create a scatter plot, we would write something like this: `ax.scatter('x', 'y', data=my_data)`.

Now, let's do some practice!

## Task

1. Create an instance of `Figure` and `Axes` in the `plot` function.
2. Create a scatter plot where the x-axis represents `user_score`, the y-axis represents `critic_score`, and the data is `games`.

Note that we have preprocessed the data for you, but if you prefer, you can do this yourself.
Please see the corresponding hint below.

## Hints

<div class="hint" title="How to run the code?">
   To run the code, click the green triangle next to the entry point. If any execution errors occur,
   they will be displayed in the console inside the IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="Where to find my figure?">
   After running the code, the graph will be generated next to the task.py file.

   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="How should I preprocess the data?">
   Before using the data, you need to perform several preprocessing steps:
   <ol>
      <li>Convert column names to lowercase.</li>
      <li>Remove games with user scores listed as "to be decided" (i.e., where the user score is <code>tbd</code>).</li>
      <li>Drop all NaN values from the following columns:</li>
      <ul>
         <li><code>critic_score</code></li>
         <li><code>user_score</code></li>
      </ul>
      <li>Convert the <code>user_score</code> column to a float.</li>
   </ol>

   Note that your own preprocessing function will not be tested.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
