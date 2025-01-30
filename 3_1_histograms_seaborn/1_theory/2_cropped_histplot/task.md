## Theory

Our first histogram didn't reveal much about the data distribution because of some extreme values. Let's look at the summary statistics to understand why:

|       | global_sales |
|:------|-------------:|
| count |        14294 |
| mean  |      0.59205 |
| std   |      1.66266 |
| min   |         0.01 |
| 25%   |         0.06 |
| 50%   |         0.19 |
| 75%   |         0.54 |
| max   |        82.53 |

While most games have sales between 0.01 and 0.54 million copies (the interquartile range), there are some games with extremely high sales (up to 82.53 million!). These outliers are stretching our histogram, making it hard to see the distribution of typical games.

To better visualize the typical distribution, we can focus on games with sales up to the 95th percentile.

## Task

Create a histogram of global sales, but only include games with sales below the 95th percentile. You can use Pandas' `quantile` method to find this threshold:
```python
threshold = games['global_sales'].quantile(0.95)
filtered_games = games[games['global_sales'] <= threshold]
```

## Hints

<div class="hint" title="What is a percentile?">
A percentile divides your data into 100 equal parts. For example, the 95th percentile is the value below which 95% of your data falls. In our case, we're excluding the top 5% of games by sales to better see the distribution of typical games.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
