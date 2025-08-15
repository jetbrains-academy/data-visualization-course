## Theory

In this dataset, there are many platforms,
making the figure difficult to interpret due to overlapping labels on the x-axis.
We can address this issue either by reducing the number of groups 
or by changing the layout of the figure, relocating the labels from the x-axis to the y-axis.

To adjust the layout of the bar chart, we need to use a different plotting method — 
[`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh).
The key differences between the `barh` and the previous `bar` function are:
1. `barh` plots horizontal bar charts, whereas `bar` builds vertical bar charts.
2. Since the layout has changed, the first argument is now `y`, and the second argument is now `width`.

After making this change, you may notice that the labels are still very close to each other.
To fix this, we can use 
the [`fig.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html) method,
which adjusts the padding between and around the elements of the figure.
Please note that we should call this method AFTER plotting all necessary data onto the figure.

## Task

Change the layout of the figure to horizontal and adjust the padding.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
