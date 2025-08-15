## Theory

Great!
Now we finally have all the regions plotted together.
However, it's not clear which trace corresponds to which region. 
Adding a legend could solve this issue.

To add a legend to our figure in Matplotlib,
we need to call the [`ax.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend) method.


However, if we do this without further adjustment, nothing will happen.
This is because Matplotlib doesn't know the names of the regions.
To fix this, we must pass the region name to the `bar` method using the `label` argument.

## Task

1. Pass the region name as the `label` argument to the `bar` method.
2. Add the legend to the figure.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
