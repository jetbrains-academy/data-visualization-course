import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate sample weather data
np.random.seed(42)
temperatures = np.random.normal(20, 5, 1000)  # Temperature data
humidity = temperatures * 2 + np.random.normal(0, 10, 1000)  # Correlated humidity data
rainfall = np.random.exponential(5, 1000)  # Rainfall data

# Create a figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# 1. Density Estimation
density = stats.gaussian_kde(temperatures)
x_range = np.linspace(temperatures.min(), temperatures.max(), 100)
ax1.plot(x_range, density(x_range))
ax1.hist(temperatures, bins=30, density=True, alpha=0.5)
ax1.set_title('Density Estimation\nof Temperature')
ax1.set_xlabel('Temperature (°C)')
ax1.set_ylabel('Density')

# 2. Cumulative Histogram
sorted_rainfall = np.sort(rainfall)
cumulative = np.arange(1, len(sorted_rainfall) + 1) / len(sorted_rainfall)
ax2.plot(sorted_rainfall, cumulative)
ax2.set_title('Cumulative Distribution\nof Rainfall')
ax2.set_xlabel('Rainfall (mm)')
ax2.set_ylabel('Cumulative Proportion')

# 3. 2D Histogram
ax3.hist2d(temperatures, humidity, bins=30, cmap='viridis')
ax3.set_title('2D Histogram of\nTemperature vs Humidity')
ax3.set_xlabel('Temperature (°C)')
ax3.set_ylabel('Humidity (%)')

plt.tight_layout()

plt.savefig("common/resources/images/histograms/4_advanced_concepts.png")
plt.show()
