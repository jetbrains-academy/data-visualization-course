## Task

As an experiment, researchers recorded changes of the subject's `y` variable by varying the `x` variable.
It was the secret research, so they haven't told us any additional information about it.
But they said they found something unusual in the observations.
The researchers approximated the data (`approximated_y`),
and now they're looking for help with plotting to see this unexpected behavior in a figure.
Let's help them!

Our figure should consist of two traces: line and scatter.
The line trace should plot approximated data, and the scatter trace should plot actual data.

You should also make several visual adjustments:

1. The line trace should bе `navy`.
2. The scatter trace should be `grey` and almost transparent (`0.05`).
3. The x-axis view should be limited to an interval from `-4` to `4`.
4. The x-axis should have only three ticks: `-4`, `0` and `4`.
5. The x-axis should be labeled as `x`.
6. The y-axis view should be limited to an interval from `-2` to `2`.
7. The y-axis should have only three ticks: `-1.5`, `0` and `1.5`.
8. The y-axis should be labeled as `y`.
9. The top and right spines should be removed.

Note that you don't need to make any preprocessing of the data.

If you get stuck,
please feel free to use hints bellow where you can also find what the final figure should look like.

## Hints

<div class="hint" title="How the figure should look like?">
    <img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to colorize the trace?">
    To colorize line or scatter you can use the <code>color</code> argument:
    <code>ax.line("x", "y", data=my_data, color="color_name")</code>
</div>

<div class="hint" title="How to make the trace transparent?">
    To make line or scatter transparent you can use the <code>alpha</code> argument:
    <code>ax.scatter("x", "y", data=my_data, alpha=0.5)</code>
</div>

<div class="hint" title="How to limit an axis view?">
    To limit an axis view you can use the <code>set_xlim</code> or <code>set_ylim</code> method of the <code>Axes</code> object:
    <code>ax.set_xlim(1, 3)</code>
</div>

<div class="hint" title="How to set ticks?">
    To set ticks you can use the <code>set_xticks</code> or <code>set_yticks</code> method of the <code>Axes</code> object:
    <code>ax.set_xticks([1, 2, 3])</code>
</div>

<div class="hint" title="How to set label for an axis?">
    To set label for an axis you can use the <code>set_xlabel</code> or <code>set_ylabel</code> method of the <code>Axes</code> object:
    <code>ax.set_xlabel("x")</code>
</div>

<div class="hint" title="How to remove spines?">
    To remove a spine you can use the <code>set_visible</code> method of the <code>Spine</code> object:
    <code>ax.spines["bottom"].set_visible(False)</code>
</div>
