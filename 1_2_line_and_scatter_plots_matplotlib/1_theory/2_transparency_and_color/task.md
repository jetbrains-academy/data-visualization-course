## Theory

Now we can see how the scores are distributed, but we can't understand the density of points because they are too
packed. To understand the density better, we can adjust the plot's transparency.

In matplotlib, you can pass the `alpha` parameter to functions to control this. It accepts a float number between 0 and 1.

Also, let's familiarize ourselves with another helpful parameter, `color`, which is used to change the color of the
plotted points, lines and shapes. It can accept many types of inputs:
* RGB or RGBA tuple of float values: `(0.1, 0.2, 0.5)` or `(0.1, 0.2, 0.5, 0.3)`.
* Case-insensitive hex RGB or RGBA string: `#0f0f0f` or `#0f0f0f80`.
* Simple colors like `red`, `green`, `blue`, etc.
* [X11 color names](https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart).
* And [much more](https://matplotlib.org/stable/users/explain/colors/colors.html#color-formats)!

## Task

Set the transparency of your `scatter` to `0.1` and colorize it with `green` color.

## Hints
<div class="hint" title="How the figure should look like?">
<img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>
