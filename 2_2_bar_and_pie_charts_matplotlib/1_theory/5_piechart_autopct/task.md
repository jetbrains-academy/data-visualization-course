## Theory

By looking at this figure, we can't tell exactly how much is each wedge,
so it would be convenient to place these numbers on the pie chart.

To do it, you can use the `autopct` argument.
It accepts a format string and applies it to each wedge size.
For example, if we pass there `%.1f%%`, we will get `32.2%` for the wedge size `32.24`,
because the format string consists of two parts:
1. `%.1f` will be converted to `32.2`.
2. `%%` will be converted to `%`.

To learn more about the format string language, 
please refer to the [documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

You can also pass a function to `autopct`, that accepts wedge size and returns a string.

## Task

Add wedge sizes to the pie chart. They should be rounded to **two decimal places** and have the `%` symbol at the end.

## Hints

<div class="hint" title="How to round wedge sized to two decimal places">
   You could you the format string from the example, but with <code>%.2f</code> instead of <code>%.1f</code>.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
