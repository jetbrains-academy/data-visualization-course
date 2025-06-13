## Theory

After applying the `stat="probability"` parameter, we notice that the overall shape of the graph remains the same. This
is because, by default, Seaborn normalizes the probability across all categories combined.

This means the probability for each bin is calculated as a fraction of the entire dataset, rather than separately
for each publisher. As a result, if one publisher has more games, its bars may still dominate the histogram, making
direct comparisons difficult.

To address this, we can use the `common_norm` parameter. When set to `False`, it ensures that each publisher’s histogram is
normalized independently, making their distributions directly comparable.

## Task

Modify the histogram so that it calculates probabilities separately for each publisher.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
