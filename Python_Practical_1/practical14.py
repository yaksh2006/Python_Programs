import math

# Normal Distribution PDF
def normal_pdf(x, mean, std_dev):
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * \
           math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))

# Input
mean = float(input("Enter mean (μ): "))
std_dev = float(input("Enter standard deviation (σ): "))
x = float(input("Enter value of x: "))

# Output
result = normal_pdf(x, mean, std_dev)

print("\n--- Normal Distribution ---")
print(f"f(x) = {result:.5f}")