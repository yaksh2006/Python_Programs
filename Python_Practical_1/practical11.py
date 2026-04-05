import math
import statistics

# Input data
data = list(map(float, input("Enter numbers separated by space: ").split()))

# Confidence level (default 95%)
confidence_level = float(input("Enter confidence level (e.g., 0.95): "))

# Z-score mapping (approx values)
z_table = {
    0.90: 1.645,
    0.95: 1.96,
    0.99: 2.576
}

# Get Z value
Z = z_table.get(confidence_level, 1.96)  # default 95%

# Calculations
mean = statistics.mean(data)
std_dev = statistics.stdev(data)  # sample standard deviation
n = len(data)

margin_error = Z * (std_dev / math.sqrt(n))

lower_bound = mean - margin_error
upper_bound = mean + margin_error

# Output
print("\n--- Confidence Interval ---")
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Sample Size:", n)
print("Z-score:", Z)
print("Confidence Interval: ({:.4f}, {:.4f})".format(lower_bound, upper_bound))