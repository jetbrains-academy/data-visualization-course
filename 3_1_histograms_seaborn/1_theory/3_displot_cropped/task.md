## Theory

By looking at the histogram with a logarithmic scale, we can clearly see that almost no games exceed
`10` million in sales. But
is this threshold sufficient? To better understand the distribution, let’s examine the summary statistics of our
dataset.

We can generate summary statistics for the `global_sales` column in the dataset using the
[`describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) method:

| parameter | global_sales |
|:----------|-------------:|
| count     |        14294 |
| mean      |      0.59205 |
| std       |      1.66266 |
| min       |         0.01 |
| 25%       |         0.06 |
| 50%       |         0.19 |
| 75%       |         0.54 |
| max       |        82.53 |

As we can see, the data contains more than `14` thousand game sales distributed between `0.01` and `82.53` million with
a mean
of approximately `0.59` million. However, there are also some unusual values specified for `25%`, `50%` and `75%`. These are called
percentiles.

A percentile represents the value below which a given percentage of data points in a dataset fall. For example, we can
see that `75%` of games have sales below `0.54` million, while the remaining `25%` have
sales ranging from
`0.54` million to `82.53` million! This creates a huge gap, making visualization difficult. 

To address this issue, let's
exclude the top `5%` of games by sales and focus on those below the 95th percentile.

## Task

Use the hidden `filter_by_global_sales` function to retrieve the dataset, including only games with sales below the 95th
percentile. Then, pass it to the `displot` function.

Please note that you don't need to apply a logarithmic scale for this task.

If you prefer, you can filter the dataset manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to import the hidden function?">
    To import it, place the cursor on the underlined hidden function name in your code, press &shortcut:ShowIntentionActions;, and
    select <samp>Import 'function_name from data'</samp>:
    <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="How to import hidden functions" style="max-height: 500px">
</div>

<div class="hint" title="How to filter the data using a percentile?">
    To filter the data, you need to:
    <ol>
    <li> Calculate the threshold using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html"><code>quantile</code></a>
    method on the <code>global_sales</code> column. Please note that the method requires a quantile, not a percentile.
    To convert a percentile to a quantile, divide it by <code>100</code>. 
    For example, the 95th percentile corresponds to a quantile of <code>0.95</code>.</li>
    <li> Filter the data by the <code>global_sales</code> column using boolean indexing.</li>
    </ol>
</div>
