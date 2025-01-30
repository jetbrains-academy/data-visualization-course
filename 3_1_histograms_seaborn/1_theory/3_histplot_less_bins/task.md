## Theory

Our histogram now shows the distribution more clearly, but it might be too detailed. When we have many bins, random variations in the data can create a "noisy" appearance that makes it harder to see the overall pattern.

The number of bins controls the trade-off between detail and smoothness:
- Too many bins: Shows more detail but can be noisy
- Too few bins: Smoother but might hide important features
- Just right: Clear pattern while preserving important details

By default, Seaborn uses a method called "Sturges' rule" to choose the number of bins, but we can override this with the `bins` parameter.

## Task

Create the same histogram as before, but set the number of bins to 20. This should give us a clearer view of the overall distribution pattern.

## Hints

<div class="hint" title="How to set the number of bins?">
The `bins` parameter in `histplot` accepts an integer specifying the number of bins:
```python
sns.histplot(data=filtered_games, x='global_sales', bins=20)
```
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
