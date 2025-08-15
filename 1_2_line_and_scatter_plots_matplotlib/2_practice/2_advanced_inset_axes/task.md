## Task

Researchers have received the figure we created for them and were very pleased with the results. But they asked us to make a
few adjustments to the figure.

First of all, researchers asked us to limit `x` axis view to the interval from `-4` to `4`, and `y` axis view to the
interval from `-2` to `2`.
We can do it
using the [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html)
or [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html) methods.

They also noticed a small spike in our data and asked us to plot this detail more closely on the same figure, so let's do that.

To achieve this, we can use _inset axes_. Please consult
the [documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html) page to figure out
how to do this.

You can place the inset axes anywhere you like and adjust the size as needed.
For example, you can place it at coordinates `(0.15, 0.7)` and set the size to `(0.3, 0.3)`.

The inset axes should display only the area of the parent axes from `x = 0.5` to `x = 1.5`, and from `y = 0.6`
to `y = 1.1`. The ticks should only mark the boundaries.

After that, we can connect our new axes with the relevant area of the parent axes using
the [`indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html)
method.

If you get stuck,
please feel free to use the hints below, where you can also find what the final figure should look like.

## Further customization

If you want, you can further customize the figure. Here are some ideas for the customization:

1. You can change the inset zoom color and style.
2. You can adjust the thickness of all lines in the figure to be uniform.
3. You can add a legend and a title.

We encourage you to explore these customizations on your own, as not all of them will be covered in the course.

Note that these changes will not be tested and might break existing tests.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to limit an axis view?">
    To limit an axis view, you can use the <code>set_xlim</code> or <code>set_ylim</code> method of the <code>Axes</code> object:
    <code>ax.set_xlim(1, 3)</code>.
</div>

<div class="hint" title="How to add the inset axes?">
    To add inset axes, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html"><code>inset_axes</code></a>
    method of the <code>Axes</code> object:
    <code>ax.inset_axes([0.1, 0.5, 0.4, 0.4])</code>.
</div>

<div class="hint" title="How to plot the data on the inset axes?">
    To plot the data on the inset axes, you can use the same methods and parameters as you would for plotting on a regular <code>Axes</code> object, since it is the same type of object:
    <code>inset_ax.scatter("x", "y", data=my_data, color="color_name", alpha=0.5)</code>.
</div>

<div class="hint" title="How to limit the inset axes area?">
    To limit the inset axes area, you can use the <code>set_xlim</code> or <code>set_ylim</code> method of the <code>Axes</code> object:
    <code>inset_ax.set_xlim(1, 3)</code>.<br><br>
    You can also set these boundries by passing the <code>xlim</code> or <code>ylim</code> parameter while creating a new inset axis:
    <code>ax.inset_ax(..., xlim=[1, 3])</code>.
</div>

<div class="hint" title="How to set the ticks on the inset axes?">
    To set the ticks on the inset axes, you can use the <code>set_xticks</code> or <code>set_yticks</code> method of the <code>Axes</code> object:
    <code>inset_ax.set_xticks([1, 2, 3])</code>.<br><br>
    You can also set these ticks by passing the <code>xticks</code> or <code>yticks</code> parameter while creating a new inset axis:
    <code>ax.inset_ax(..., xticks=[1, 2, 3])</code>.
</div>

<div class="hint" title="How to connect the inset axes with the parent axes area?">
    To connect the inset axes with the parent axes area, you can use the <code>indicate_inset_zoom</code> method of the <code>Axes</code> object:
    <code>ax.indicate_inset_zoom(inset_ax)</code>.
</div>
