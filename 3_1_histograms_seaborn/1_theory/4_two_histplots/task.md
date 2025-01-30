## Theory

Now that we understand how to create basic histograms, let's use them to compare distributions. For example, we might want to compare the sales distributions of games from different publishers or on different platforms.

Seaborn's `histplot` can plot multiple distributions in several ways:
1. Side by side using multiple axes
2. Overlaid on the same axis with transparency
3. Stacked on top of each other

We'll focus on overlaid histograms, which are great for direct comparisons. To create them, we can use the `hue` parameter to specify which column should be used to split the data into groups.

## Task

Create a histogram comparing the sales distributions of Nintendo and Electronic Arts games. Use the `publisher` column with the `hue` parameter to differentiate between publishers.

To make the comparison clearer:
1. Filter the data to include only these two publishers
2. Keep only games with sales below the 95th percentile
3. Set `alpha=0.5` for some transparency
4. Use 20 bins as we did before

## Hints

<div class="hint" title="How to filter for specific publishers?">
You can use boolean indexing to select specific publishers:
```python
publishers = ['Nintendo', 'Electronic Arts']
filtered_games = games[games['publisher'].isin(publishers)]
```
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
