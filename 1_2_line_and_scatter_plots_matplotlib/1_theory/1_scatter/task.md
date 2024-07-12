## Goal

The main goal of the lesson is to **plot the correlation between the user score and the critic score**.

## Theory


## Task

Modify the `plot` by adding a call of the `scatter` method there.
Pass `games` there as data, `user_score` as x-axis, and `critic_score` as y-axis to it.

Note that we preprocessed the data for you, but if you want, you can do this by yourself.
Please see the corresponding hint below.

## Hints

<div class="hint" title="How to run the code?">
To run the code, you should click on the green triangle next to the entry point. In case of execution errors,
they will be shown in the console inside the IDE. 
<img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="Where to find my figure?">
After running the code, the graph will be generated next to the task.py file.
<img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="How should I preprocess the data?">
Before using the data, we need to make several preprocessing steps:
<ol>
   <li>Lower column names.</li>
   <li>Remove games with user scores to be decided (the user score is equal to <code>tbd</code>).</li>
   <li>Drop all nans.</li>
   <li>Convert the <code>user_score</code> column to float.</li>
</ol>

If you have some difficulties with your own preprocessing, you can
have [a sneak to the inner file](file://1_2_line_and_scatter_plots_matplotlib/1_theory/1_scatter/data.py)
where our preprocessing is defined.
</div>

<div class="hint" title="How the figure should look like?">
<img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>
