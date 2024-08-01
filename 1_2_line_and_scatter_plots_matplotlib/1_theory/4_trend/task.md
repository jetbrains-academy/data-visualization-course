## Theory

Let's try to understand what is going on in our graph.
Our data consists of pairs of user scores and critic scores.
For each user score, several critic scores might exist: for example, if we have two games with equal user scores,
they can have different critic scores because it is different games.

However, matplotlib doesn't do additional preprocessing, 
so the `plot` method just connects those points in the order in which they located in our dataset.
That's why we got this strange "yarn ball".

To address this issue, we need to do the preprocessing ourselves.
For example, we can calculate the mean critic score for each user score.

## Task

Add a call of the hidden `aggregate` function.
This function will calculate the mean and return the table with columns: `user_score` and `critic_score`.

If you want, you can aggregate the data by yourself. Please see the corresponding hint below.

## Hints

<div class="hint" title="How the figure should look like?">
   <img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I aggregate the data?">
   To aggregate the data, we can use pandas:
  
   <ol>
   <li>Group the data by the <code>user_score</code> column.</li>
   <li>Use the mean for the <code>critic_score</code> column as an aggregating function.</li>
   <li>Reset the index to convert a series to a dataframe.</li>
   </ol>
    
   If you have some difficulties with your own aggregation, you can
   have [a sneak peek into the file](file://1_2_line_and_scatter_plots_matplotlib/1_theory/4_trend/data.py)
   where our preprocessing is defined.

   Note that your own aggregation function will not be tested.
</div>
