## Theory

Finally, we can see all the platform names, 
but the current data does not clearly show what percentage each platform represents compared to the others.

Luckily, the count plot has a special argument called `stat`, which modifies the calculated statistics.
This argument accepts the following values:
1. `count`: The number of observations per category.
2. `proportion`: Similar to `count`, but normalized so that all bars sum to `1`.
3. `percent`: Similar to `count`, but normalized so that all bars sum to `100`.
4. `probability`: An alias for `proportion`.

## Task

Update the statistic by setting it to `percent`.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
