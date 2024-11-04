# Understanding Data Distribution with Histograms

When Andy first started his job at the weather station, he was overwhelmed by the sheer amount of rainfall data collected over the years. Just looking at the raw numbers made his head spin! That's when his mentor introduced him to histograms - a visualization tool that would change the way he looked at data forever.

## What is a Histogram?

Think of a histogram as a story of your data. For Andy, each bar in his rainfall histogram told him how many days had similar amounts of precipitation. Here's how it works:

1. Divide the range of values into equal-width intervals (called "bins")
2. Count how many data points fall into each bin
3. Create rectangular bars where:
   - Height shows how many items are in each bin
   - Width represents the bin interval
   - Area of each bar is proportional to the frequency

## Why Use Histograms?

Andy discovered that histograms were invaluable when he needed to:
- Spot rainfall patterns that weren't obvious in raw numbers
- Identify unusual weather events
- Compare this year's precipitation with historical patterns
- Plan for potential flood seasons

## What Can We Learn from a Histogram?

Through his daily work, Andy learned that a histogram reveals several crucial characteristics:

1. **Central Tendency**
   - Where most rainy days cluster
   - Whether there's one typical rainfall amount (unimodal) or several common amounts (multimodal)

2. **Spread**
   - How variable the rainfall is
   - Whether some months have more consistent rainfall than others

3. **Shape**
   - Symmetry: Are extreme rainfall events equally likely on both sides?
   - Skewness: Are heavy rains (right skew) or light drizzles (left skew) more common?
   - Kurtosis: How frequent are extreme weather events?

4. **Unusual Features**
   - Drought periods (gaps in the data)
   - Record-breaking storms (outliers)
   - Distinct weather patterns (multiple groups)

## Historical Note

The word "histogram" was first coined by Karl Pearson in 1891. The name combines the Greek "histos" (anything set upright) and "gramma" (drawing, record). Pearson might never have imagined how his invention would help future meteorologists like Andy make sense of complex weather patterns!

<img src="../../common/resources/images/histograms/1_1d_histograms_theory.png">

Let's follow Andy's journey as he learns to create and interpret histograms using Python's powerful visualization libraries: Seaborn and Matplotlib.
