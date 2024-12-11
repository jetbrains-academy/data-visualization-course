## Theory

Now we have no so many classes, and it could be more convenient to represent the same data in the form of pie chart,
because the proportion is more relevant for us rather than the absolute values.

To make a pie chart using Matplotlib, we might use 
the [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html) function.
It accepts three main arguments:
* `x`: A collection of wedge sizes.
* `label`: A collection of labels for each wedge.
* `data`: The input data structure.

Please note that you don't need to normalize the passed values,
since Matplotlib will automatically divide each element of `x` by `sum(x)`.

## Task

Replace the call of the `barh` function with the `pie` function.
Pass there `count` as the wedge sizes and `platform` as the labels and `games` as the data.

Please note that you don't need to customize the figure for now.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
