# # for discrete
# # Discrete Distribution (PMF)

# n = int(input("Enter number of values: "))

# values = []
# probabilities = []

# print("Enter values and their probabilities:")
# for i in range(n):
#     x = float(input(f"Value {i+1}: "))
#     p = float(input(f"Probability of {x}: "))
#     values.append(x)
#     probabilities.append(p)

# # Check sum of probabilities
# total_prob = sum(probabilities)

# print("\n--- Discrete Distribution ---")
# for i in range(n):
#     print(f"P(X = {values[i]}) = {probabilities[i]}")

# print("\nTotal Probability =", total_prob)

# if abs(total_prob - 1) < 0.0001:
#     print("Valid Distribution ✅")
# else:
#     print("Invalid Distribution ❌ (Sum must be 1)")

# for contineous
import math

# Continuous Distribution (example PDF: f(x) = 2x in [0,1])

def pdf(x):
    if 0 <= x <= 1:
        return 2 * x
    else:
        return 0

# Input
x = float(input("Enter value of x (0 to 1): "))

# Output
print("\n--- Continuous Distribution ---")
print(f"f(x) = {pdf(x)}")

# Approximate integration (area under curve)
steps = 1000
a, b = 0, 1
dx = (b - a) / steps

area = 0
for i in range(steps):
    xi = a + i * dx
    area += pdf(xi) * dx

print("Total Area under curve (approx):", area)