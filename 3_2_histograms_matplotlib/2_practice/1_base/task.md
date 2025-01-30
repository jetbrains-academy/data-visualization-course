## Theory

While Seaborn provides a high-level interface for creating histograms, Matplotlib offers more fine-grained control over the visualization. This can be useful when you need to:

1. Customize specific aspects of the plot
2. Create complex layouts
3. Combine histograms with other Matplotlib plots
4. Optimize performance for large datasets

In Matplotlib, histograms are created using the `hist` method of the `Axes` object. Key parameters include:
- `bins`: Number of bins or bin edges
- `density`: Whether to normalize the histogram
- `alpha`: Transparency
- `color`: Bar color
- `label`: Legend label

## Task

Create a histogram comparing Nintendo and EA games using Matplotlib:
1. Use the preprocessed data from previous tasks
2. Set 20 bins
3. Show probabilities instead of counts
4. Use alpha=0.5
5. Add a legend
6. Label axes appropriately

## Hints

<div class="hint" title="How to create a histogram in Matplotlib?">
```python
# Create figure and axes
fig, ax = plt.subplots()

# Plot histogram for each publisher
for publisher in ['Nintendo', 'Electronic Arts']:
    publisher_data = processed_data[processed_data['publisher'] == publisher]
    ax.hist(publisher_data['global_sales'], bins=20, density=True, alpha=0.5, label=publisher)

# Add legend
ax.legend()
```
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>