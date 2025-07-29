## Theory

Let's try to understand what is going on in our graph.
Our data consists of pairs of user scores and critic scores.
For each user score, there may be multiple critic scores: for example, if we have two games with the same user score,
they can have different critic scores because they are different games.

However, Matplotlib doesn't perform additional preprocessing,
so the `plot` method simply connects the points in the order they appear in the dataset.
This is why we end up with a confusing "yarn ball" effect.

To address this issue, we need to preprocess the data ourselves.
For example, we can calculate the mean critic score for each user score.

## Task

Add a call of the hidden `aggregate` function.
This function will calculate the mean and return a table with columns: `user_score` and `critic_score`.

If you prefer, you can aggregate the data yourself. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to import hidden functions?">
    To import it, you can place the cursor on the underlined hidden function name in your code, then press &shortcut:ShowIntentionActions;, and
    select <samp>Import 'function_name from data'</samp>:
    <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I aggregate the data?">
   To aggregate the data, you can use Pandas:

   <ol>
   <li>Group the data by the <code>user_score</code> column.</li>
   <li>Use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.mean.html"><code>mean</code></a> method to aggregate the <code>critic_score</code> column. </li>
   <li>Reset the index to convert the series into a DataFrame.</li>
   </ol>

Note that your own aggregation function will not be tested.
</div>
