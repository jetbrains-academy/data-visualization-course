import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create figure with subplots
plt.figure(figsize=(15, 10))

# 1. Symmetric (Normal) Distribution
data_symmetric = np.random.normal(loc=0, scale=1, size=1000)
plt.subplot(2, 3, 1)
plt.hist(data_symmetric, bins=30, color="#B3B3FF", edgecolor="black")
plt.title("Symmetric")
plt.xlabel("Value")
plt.ylabel("Frequency")

# 2. Left-skewed Distribution
data_left_skewed = -np.random.beta(a=5, b=2, size=1000) * 10
plt.subplot(2, 3, 2)
plt.hist(data_left_skewed, bins=30, color="#B3B3FF", edgecolor="black")
plt.title("Left-skewed")
plt.xlabel("Value")
plt.ylabel("Frequency")

# 3. Right-skewed Distribution
data_right_skewed = np.random.beta(a=2, b=5, size=1000) * 10
plt.subplot(2, 3, 3)
plt.hist(data_right_skewed, bins=30, color="#B3B3FF", edgecolor="black")
plt.title("Right-skewed")
plt.xlabel("Value")
plt.ylabel("Frequency")

# 4. Bimodal Distribution
data_bimodal = np.concatenate(
    [
        np.random.normal(loc=-2, scale=0.5, size=500),
        np.random.normal(loc=2, scale=0.5, size=500),
    ],
)
plt.subplot(2, 3, 4)
plt.hist(data_bimodal, bins=30, color="#B3B3FF", edgecolor="black")
plt.title("Bimodal")
plt.xlabel("Value")
plt.ylabel("Frequency")

# 5. Multimodal Distribution
data_multimodal = np.concatenate(
    [
        np.random.normal(loc=-4, scale=0.5, size=300),
        np.random.normal(loc=0, scale=0.5, size=400),
        np.random.normal(loc=4, scale=0.5, size=300),
    ],
)
plt.subplot(2, 3, 5)
plt.hist(data_multimodal, bins=30, color="#B3B3FF", edgecolor="black")
plt.title("Multimodal")
plt.xlabel("Value")
plt.ylabel("Frequency")

# 6. Uniform Distribution
data_uniform = np.random.uniform(low=-5, high=5, size=1000)
plt.subplot(2, 3, 6)
plt.hist(data_uniform, bins=30, color="#B3B3FF", edgecolor="black")
plt.title("Uniform")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Adjust layout and display
plt.tight_layout()
plt.savefig("common/resources/images/histograms/2_distribution_shapes.png")

plt.show()

# Save the plot
plt.close()

# Create a second figure with different distributions
plt.figure(figsize=(15, 5))

# Generate and plot different distributions
distributions = {
    "Normal": np.random.normal(0, 1, 1000),
    "Exponential": np.random.exponential(1, 1000),
    "Uniform": np.random.uniform(-3, 3, 1000),
}

for i, (name, data) in enumerate(distributions.items(), 1):
    plt.subplot(1, 3, i)
    plt.hist(data, bins=30, color="#B3B3FF", edgecolor="black")
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("common/resources/images/histograms/1_different_distribution.png")

plt.show()

# Save the second plot
plt.close()
