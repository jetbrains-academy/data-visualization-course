## Theory

Looking at the current figure, we can't easily determine the exact size of each wedge.
It would be convenient to place these numbers directly on the pie chart.

To do this, we can use the `autopct` argument.
It accepts a format string and applies it to each wedge size.
For example, if we pass `%.1f%%` as the format string, a wedge with a size of `32.24` will be displayed as `32.2%`.
Here's how the format string works:

1. `%.1f` is converted to `32.2`.
2. `%%` is converted to `%`.

Please refer to the corresponding hint bellow for more details on formatting floating-point numbers.

## Task

Add wedge sizes to the pie chart. They should be rounded to **two decimal places** and have a `%` symbol at the end.

## Hints

<div class="hint" title="Additional formating details">

- **Floating-point numbers**: The `%.1f` in the format string specifies that the number should be displayed with one
  decimal
  place. You can adjust this to display more or fewer decimal places, e.g., `%.2f` for two decimal places or `%.0f` for
  none
  (effectively rounding to the nearest whole number).
- **Percentage sign**: `%%` in the format string is used to display a percentage sign. This is because `%`
  
  is a special character in Python strings, so if you want to display it, you need to use `%%`.

You can also pass a function to `autopct`, which accepts the wedge size and returns a string.

To learn more about the format string language, please refer to
the [documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

</div>

<div class="hint" title="How to round wedge sizes to two decimal places?">
   You can use the format string from the example, but replace <code>%.1f</code> with <code>%.2f</code>.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
