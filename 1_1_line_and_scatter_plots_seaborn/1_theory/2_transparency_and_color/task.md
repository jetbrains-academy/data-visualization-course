## Theory

We can now see how the scores are distributed,
but the points are too closely packed to understand their density clearly.
To better visualize the density, we can adjust the plot's transparency.

In Seaborn, we can use the `alpha` parameter to control transparency.
This parameter accepts a float value between 0 and 1.

Let's also explore another useful parameter, `color`,
which allows you to change the color of plotted points, lines and shapes.
This parameter can accept a variety of inputs, such as:
* An RGB or RGBA tuple of float values, e.g., `(0.1, 0.2, 0.5)` or `(0.1, 0.2, 0.5, 0.3)`.
* A case-insensitive hex RGB or RGBA string, e.g., `#0f0f0f` or `#0f0f0f80`.
* Simple color names like `red`, `green`, `blue`, etc.
* [X11 color names](https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart).
* And [much more](https://matplotlib.org/stable/users/explain/colors/colors.html#color-formats)!

## Task

Set the transparency of your `relplot` to `0.1` and color it `green`.

## Hints
<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
