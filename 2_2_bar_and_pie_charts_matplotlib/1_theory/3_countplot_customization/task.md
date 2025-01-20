## Theory

Now the figure looks good, but there is still some space for improvements.

First, there are a lot of gaming platforms, and most of them are ancient,
so let's focus only on modern platforms like `WiiU`, `PS4`, `XOne` and `PC`.

Second, each of these platforms has its own brand color,
so it would be convenient to color each bar accordingly.
To change a color of bars, we should use the `color` argument. It accepts:
1. A single color. In this case, each bar will be colored in the specified color.
2. A collection of colors. In this case, these colors will be applied to the corresponding bars. 
   But note that since our bar chart is horizontal, colors will be applied from bottom to top.

We have described the format in which colors might be defined in detail in the
"[Line and Scatter Plots](course://1_2_line_and_scatter_plots_matplotlib/1_theory/2_transparency_and_color)" lesson.

And the last thing, it will be great to have captions for axes and the figure.

## Task

1. Use the hidden `filter_platforms` function to filter all platforms out except for `WiiU`, `PS4`, `XOne` and `PC`.
   
   If you prefer, you can do it yourself. Please refer to the corresponding hint below.

2. Color the bars in the following way: `WiiU` with `cyan`, `PS4` with `blue`, `XOne` with `green` and `PC` with `grey`.
3. Set the x-axis label to `Count`.
4. Set the y-axis label to `Platform`.
5. Set the figure title to `Number of games per platform`.

## Hints

<div class="hint" title="How should I filter the platforms?">
    To filter out the unnecessary platforms you can use
    the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html"><code>is_in</code></a> function
    on the <code>platform</code> column.

   Note that your own function will not be tested.
</div>

<div class="hint" title="How to set a label for an axis?">
    To set a label for an axis,
    you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html"><code>set_xlabel</code></a>
    or <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html"><code>set_ylabel</code></a> method:
    <code>ax.set_xlabel("x")</code>.
</div>

<div class="hint" title="How to set a title for a figure?">
    To set a title for a figure, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a> method:
    <code>ax.set_title("Title")</code>.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
