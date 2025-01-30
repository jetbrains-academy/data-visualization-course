## Theory

So far, we've been preprocessing our data right before plotting. While this works, it's often better to prepare your data first and then focus on visualization. This approach has several benefits:

1. Cleaner, more maintainable code
2. Ability to reuse the processed data
3. Easier to experiment with different visualizations
4. Better performance when working with large datasets

Let's create a function that handles all our preprocessing steps:
1. Filtering for specific publishers
2. Removing outliers
3. Any other data cleaning we might need

## Task

Create a function called `preprocess_data` that takes the games DataFrame and returns a filtered version:
```python
def preprocess_data(df):
    # Filter for Nintendo and EA
    publishers = ['Nintendo', 'Electronic Arts']
    filtered = df[df['publisher'].isin(publishers)]
    
    # Remove outliers
    threshold = filtered['global_sales'].quantile(0.95)
    filtered = filtered[filtered['global_sales'] <= threshold]
    
    return filtered
```

Then use this processed data to create the same probability histogram as before:
- 20 bins
- Alpha set to 0.5
- Publisher as the hue
- Probability statistic

## Hints

<div class="hint" title="Why preprocess data separately?">
Separating data preprocessing from visualization makes your code:
1. More readable - each part has a clear purpose
2. More maintainable - easier to modify preprocessing steps
3. More reusable - can use the same processed data for different visualizations
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
