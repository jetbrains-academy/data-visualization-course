## Task

The company appreciated our initial histogram visualization but now wants deeper insights into their sales data. While
the overlapping histograms provide a good overview of the overall distributions, they are particularly interested in
seeing how individual sales data points are positioned and identifying the median sales value for each city.

To achieve this, we will enhance our visualization with two main adjustments:

First, let's add a one-dimensional scatter plot above the existing one:

1. Create two `ax` objects using the [
   `plt.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html) function instead of a
   single one. Set `height_ratios` to `[1, 10]`.
2. Plot the data points on the corresponding `ax` object. Since it is a one-dimensional plot, the `y` coordinate
   should be the same for all points in the same city: let the `y`
   coordinate for the Belgrade sales distribution be `0.2`, and `0.1` for the Yerevan distribution.
3. Yerevan's data should be colored `crimson`, and Belgrade's data should be colored `black`.
4. Set the `alpha` parameter to `0.05`.
5. Limit the `y` axis range from `0` to `0.3`.
6. Remove both the `x` and `y` ticks.
7. Hide all spines of this plot.

Second, let's change the main histogram axes. We will add vertical lines with
text labels indicating the median sales value for each city:

1. Use the same colors as in the scatter plot for each city.
2. Draw a vertical line at each median using the [
   `axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html) method on the
   corresponding axes.
3. Make the lines dashed, set their width to `1.5`, and match their color to the corresponding histogram color.
4. Use the [
   `text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html) method to add the median values near the
   lines:
    - For Belgrade's sales: set `x`  to the median sales value _plus_ `25`, `y` to `0.005`, and the horizontal alignment to
      `left`.
    - For Yerevan's sales: set `x`  to the median sales value _minus_ `25`, `y` to `0.005`, and the horizontal alignment to
      `right`.
5. Do not include the medians in the legend.
6. Remove the axes' title and instead add a super title to the figure using the [
   `fig.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle)
   method.

Please consult the corresponding documentation pages to figure out how to do it.

You can use the hidden `get_median` function, accepting the city sales to calculate the median sales for each city.

If you get stuck,
please feel free to use the hints below, where you can also find a preview of the final figure.

## Further customization

If you want, you can further customize the figure. Here are some ideas for customization:

1. Change font weights and sizes.
2. Add minor ticks to the `x` axis of the histograms.
3. Add some jitter to the `y` axis of the scatter plot.

We encourage you to explore these customizations on your own, as not all of them will be covered in this course.

Note that these changes will not be tested and might break existing tests.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to create two axes and set height ratios?">
    You can use the 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html"><code>plt.subplots</code></a>
    function and specify the <code>height_ratios</code> parameter:
    <code>fig, (ax1, ax2) = plt.subplots(2, 1, height_ratios=[1, 10])</code>.
</div>

<div class="hint" title="How to plot a scatter plot?">
    You can use the 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter">
    <code>scatter</code></a> method on the corresponding <code>ax</code> object:
    <code>ax.scatter(x, y)</code>.
</div>

<div class="hint" title="How to generate y-coordinates for the scatter plot?">
    You can use Python list operations to make a list of constant values: <code>[1] * 10</code> will create a list of 
    <code>10</code> ones. You can also use the <code>len</code> function to get the length of the sales data: <code>len(sales)</code>.
</div>

<div class="hint" title="How to limit the y-axis view?">
    You can use the 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html"><code>set_ylim()</code></a>
    method of the <code>ax</code> object:
    <code>ax.set_ylim(1, 3)</code>.
</div>

<div class="hint" title="How to remove ticks?">
    You can remove both <code>x</code> and <code>y</code> ticks by calling the 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html"><code>set_yticks</code>
    </a> and <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html"><code>
    set_xticks</code></a> methods of the axes: <code>ax.set_yticks([])</code> and <code>ax.set_xticks([])</code>.
</div>

<div class="hint" title="How to hide all spines of a plot?">
    You can call <code>ax.spines[["top", "bottom", "left", "right"]].set_visible(False)</code> on the corresponding <code>ax</code> object.
</div>

<div class="hint" title="How to find the median of an array?">
    You can use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html"><code>median</code></a> 
    method of a Series.
</div>

<div class="hint" title="How to customize a vertical line?">
    You can change the line appearance with the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html"><code>axvline</code></a> method by setting the following three parameters: use
    <code>linestyle</code> to define the line style, <code>width</code> to configure its thickness, and <code>color</code> 
    to assign its color.
</div>

<div class="hint" title="How to exclude some elements from the legend?">
    You can retrieve the handles and labels of the legend by calling the 
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html">
    <code>get_legend_handles_labels</code></a> on the corresponding axes. 
    Then, to exclude some elements from the legend, you can pass the filtered lists of handles and labels to the <code>legend</code> method:
    <code>ax.legend(handles_filtered, labels_filtered)</code>.
</div>

<div class="hint" title="How to add a super title to the figure?">
    You can call the
    <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle">
    <code>suptitle</code></a> method on the figure object:
    <code>fig.suptitle("Title")</code>.
</div>
