## Theory

Histograms are powerful on their own, but they become even more useful when combined with other types of plots. For example, we might want to:

1. Show distributions alongside a scatter plot to understand the spread of each variable
2. Compare distributions before and after data transformations
3. Visualize how distributions change across different categories

Seaborn provides several functions for creating such combined visualizations:
- `jointplot`: Shows a scatter plot with marginal histograms
- `pairplot`: Creates a matrix of scatter plots and histograms
- `displot`: Offers flexible distribution visualization

## Task

Create a joint plot showing:
- A scatter plot of user scores vs critic scores
- Histograms of both variables on the margins

Use the preprocessed data from the previous task and:
1. Set alpha to 0.5 for the scatter plot
2. Use 20 bins for both histograms
3. Set the figure size to (10, 10)

## Hints

<div class="hint" title="How to create a joint plot?">
Use Seaborn's `jointplot` function:
```python
sns.jointplot(
    data=processed_data,
    x='user_score',
    y='critic_score',
    height=10
)
```
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>