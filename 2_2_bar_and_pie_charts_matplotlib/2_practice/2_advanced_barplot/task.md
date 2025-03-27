## Task

The organizers liked our figure but asked us to make it more readable.
Specifically, they don't like that it is hard to find the exact value for each product 
and that the legend items are in reverse order.
Let's fix the issues!

First, let's add minor ticks to the bottom x-axis and duplicate all ticks to the top axis:
1. To add minor ticks, you can use
   the familiar [`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html) method.
   Distribute these ticks from `0` to `100` with a step of `5`.
2. To duplicate the bottom ticks to the top, you can use
   the [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html) method.

Second, let's add a textual value for each product.
You can use the [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html) method to do it.
Position the text to the right of each bar's top
(the `x` coordinate should be `1` more than the number of participants, and `y` should match the position of the bar).
Round each value to one digit after the decimal point.

And last thing: to rearrange the legend items, we can use
the [`get_legend_handles_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html) method
along with the [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html) method.

Please consult the corresponding documentation pages to figure out how to do it.

If you get stuck,
please feel free to use the hints below, where you can also find what the final figure should look like.

## Further customization

If you want, you can further customize the figure. Here are some ideas for the customization:

1. Change font weights and sizes.
2. Move legend items to the y-axis.
3. Plot categories on different axes within the same figure.

We encourage you to explore these customizations on your own, as not all of them will be covered in this course.

Note that these changes will not be tested and might break existing tests.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to add minor ticks?">
    To add minor ticks, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html"><code>set_xticks</code></a> method with the <code>minor</code> argument:
    <code>ax.set_xticks([1, 2, 3], minor=True)</code>.
</div>

<div class="hint" title="How to add ticks to the top spine?">
    To add ticks to the top spine, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html"><code>tick_params</code></a> method:
    <code>ax.tick_params(top=True, labeltop=True, axis="x", which="both")</code>.
</div>

<div class="hint" title="How to add a textual value for each product?">
    To add a textual value for each product, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html"><code>text</code></a> method
    along with the <code>round</code> function for value formatting:
    <code>ax.text(value + 1, bar_y_position, f"{round(value, 1)}", verticalalignment="center")</code>.<br><br>
    Note that we use the <code>verticalalignment</code> argument here to properly align the text.
</div>

<div class="hint" title="Hot to rearrange the legend items?">
    To get a list of the legend handles and labels, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html"><code>get_legend_handles_labels</code></a> method:
    <code>handles, labels = ax.get_legend_handles_labels()</code>.<br><br>
    After that, we can pass the reversed values to the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html"><code>legend</code></a> method:
    <code>ax.legend(reversed(handles), reversed(labels))</code>
</div>
