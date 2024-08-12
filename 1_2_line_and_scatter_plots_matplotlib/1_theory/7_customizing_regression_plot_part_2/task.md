## Theory

Now the figure looks good, but let's fine-tune it a little bit.

For example, our figure doesn't have axis labels. To set them, we can
use the [`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html)
and [`set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html) methods.

We can also adjust how the ticks are distributed. To manually set tick positions, we can pass the desired tick values to
the [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html)
and [`set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html) methods.

Another useful feature to be aware of is limiting the view range of the x-axis and y-axis. To do this, we can
use the [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html)
and [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html) methods, respectively.

Our figure currently looks like it is "trapped" inside a box. 
These black lines that surround the figure are called 
[`spines`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine),
and there are four of them: `top`, `bottom`, `left`, and `right`.
We can refer to them in the following ways: `ax.spines['left']` or `ax.spines[['left', 'right']]`.
To make them disappear, we should call the `set_visible` method with the argument `False`.

## Task

1. Change the x-label to `User Score` and the y-label to `Critic Score`.
2. Set the ticks on the x-axis from `0` to `10` without skips. 
3. Set the ticks on the y-axis from `0` to `100` at intervals of `10`.
4. Remove the top and right spines from the figure.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
