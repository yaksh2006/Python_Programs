import math

# Poisson Probability Function
def poisson_probability(lmbda, k):
    return (math.exp(-lmbda) * (lmbda ** k)) / math.factorial(k)

# Input
lmbda = float(input("Enter lambda (average rate): "))
max_k = int(input("Enter max value of k: "))

print("\n--- Poisson Distribution ---")
for k in range(max_k + 1):
    prob = poisson_probability(lmbda, k)
    print(f"P(X = {k}) = {prob:.5f}")