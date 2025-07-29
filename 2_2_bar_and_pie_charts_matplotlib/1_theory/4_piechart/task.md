## Theory

Now that we have fewer categories, it may be more convenient to represent the same data as a pie chart.
This is because proportions are more relevant to us than the absolute values.

To make a pie chart using Matplotlib, we can use 
the [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie) method.
It accepts three main arguments:
* `x` — A collection of wedge sizes.
* `labels` — A collection of labels for each wedge (must be passed as a keyword argument).
* `data` — The input data structure.

Please note that you don't need to normalize the passed values,
as Matplotlib will automatically divide each element of `x` by `sum(x)`.

## Task

1. Replace the call to the `barh` method with the `pie` method.
2. Pass `count` as the wedge sizes, `platform` as the labels, and `games` as the data.

Please note that you don't need to customize the figure at this stage.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
