import math

# Function to calculate nCr
def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Binomial Probability Function
def binomial_probability(n, k, p):
    return nCr(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Input
n = int(input("Enter number of trials (n): "))
p = float(input("Enter probability of success (p): "))

print("\n--- Binomial Distribution ---")
for k in range(n + 1):
    prob = binomial_probability(n, k, p)
    print(f"P(X = {k}) = {prob:.5f}")