## Theory

Now, the figure looks good, but there is still room for improvement.

First, let's color the wedges using brand colors,
just as we did with the bar chart.
However, note that the argument to specify colors in a pie chart is called <code>color**s**</code>, not `color`!

Second, now the wedges look too packed. To add some space between them,
we can use the `explode` argument.
It accepts a collection of floats specifying the fraction of the radius by which to offset each wedge.

Finally, let's add a title to our figure and tighten its layout.

## Task

1. Color the wedges in the following way: `PC` with `grey`, `PS4` with `blue`, `XOne` with `green`, and `WiiU` with `cyan`.
2. Offset each wedge by `0.01`.
3. Set the figure title to `Proportion of games per platform`.
4. Tighten the layout.

## Hints

<div class="hint" title="How to set a title for a figure?">
    To set a title for a figure, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a> method:
    <code>ax.set_title("Title")</code>.
</div>

<div class="hint" title="How to tighten the layout?">
   To tighten the layout, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html"><code>tight_layout</code></a> method: <code>fig.tight_layout()</code> method.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
