import statistics
from collections import Counter

# Input data
data = list(map(int, input("Enter numbers separated by space: ").split()))

# 1. Distribution (frequency of each value)
distribution = Counter(data)

# 2. Mean
mean_value = statistics.mean(data)

# 3. Median
median_value = statistics.median(data)

# 4. Mode (handle multiple modes)
try:
    mode_value = statistics.mode(data)
except statistics.StatisticsError:
    mode_value = statistics.multimode(data)

# 5. Standard Deviation
std_dev = statistics.stdev(data)  # sample standard deviation

# Output
print("\n--- Results ---")
print("Data:", data)

print("\nDistribution (Frequency):")
for key, value in distribution.items():
    print(f"{key}: {value}")

print("\nMean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Standard Deviation:", std_dev)