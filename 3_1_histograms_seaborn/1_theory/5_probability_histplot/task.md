## Theory

When comparing distributions with different sample sizes, using raw counts can be misleading. For example, if one publisher has released many more games than another, its bars will naturally be higher even if the distribution shape is similar.

To address this, we can normalize the histograms so they show proportions (or probabilities) instead of counts. This makes the distributions directly comparable regardless of sample size.

In Seaborn's `histplot`, we can do this by setting the `stat` parameter to:
- `'count'` (default): Shows the number of observations in each bin
- `'probability'`: Shows the proportion of observations in each bin
- `'density'`: Similar to probability but normalized so the total area equals 1
- `'frequency'`: Like count but normalized by bin width

## Task

Modify your previous histogram to show probabilities instead of counts. Keep all other parameters the same:
- Filter for Nintendo and Electronic Arts
- Include only games below the 95th percentile of sales
- Use 20 bins
- Set alpha to 0.5

## Hints

<div class="hint" title="How to show proportions?">
Add the `stat='probability'` parameter to your `histplot` call:
```python
sns.histplot(..., stat='probability')
```
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
