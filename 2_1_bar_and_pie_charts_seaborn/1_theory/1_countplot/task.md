## Goal

The main goal of the lesson is to **plot the descriptive statistics about different game platforms and global sales**:
1. Number of different platforms
2. Total global sales per platform
3. Total sales per decade for each region

Seaborn doesn't allow plotting pie charts, so the lesson will be focused only on building bar charts.
If you want to learn how to plot a pie chart,
please see [the Matplotlib lesson](course://2_2_bar_and_pie_charts_matplotlib/1_theory/1_countplot).

## Theory

In Seaborn there is one universal function that can build almost any kind of categorical plot:
[`catplot`](https://seaborn.pydata.org/generated/seaborn.catplot.html).
As [`relplot`](https://seaborn.pydata.org/generated/seaborn.relplot.html), it accepts special argument, `kind`, 
that defines which type of plot will be built. 

In this section, we will focus on two kinds of categorical plots:
1. `bar`: it can plot general purpose bar charts 
2. `count`: it can plot a special form of a bar chart called **count plot**,
   where y-axis represents number of observations for each category.

As other Seaborn functions, `catplot` accepts three main arguments: `data`, `x` and `y`.
We described them in detail in the 
"[Line and Scatter Plots](course://1_1_line_and_scatter_plots_seaborn/1_theory/1_relplot_scatter)" section.

## Task

Use the `catplot` function to build a simple count plot.
Pass `games` there as the data, `platform` as the x-axis, and `count` as the kind.

Note that we preprocessed the data for you. To learn how we do it, please see the corresponding hint below.

## Hints
<div class="hint" title="How to run the code?">
   To run the code, click the green triangle next to the entry point.
   In case of execution errors, they will be displayed in the console inside the IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="Where to find my figure?">
   After running the code, the graph will be generated next to the <code>task.py</code> file.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="How the data was preprocessed?">
   Before using the data, we need to perform several preprocessing steps:
   <ol>
      <li>Convert column names to lowercase.</li>
      <li>Drop all NaN values from the following columns:</li>
      <ul>
         <li><code>platform</code></li>
         <li><code>year_of_release</code></li>
         <li><code>global_sales</code></li>
         <li><code>eu_sales</code></li>
         <li><code>jp_sales</code></li>
         <li><code>na_sales</code></li>
         <li><code>other_sales</code></li>
      </ul>
      <li>Convert the <code>year_of_release</code> column to an integer.</li>
   </ol>
</div>

<div class="hint" title="What should the figure look like?"> 
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
