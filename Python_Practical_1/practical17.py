# Simple Linear Regression

n = int(input("Enter number of data points: "))

X = []
Y = []

print("Enter values of X:")
for i in range(n):
    X.append(float(input()))

print("Enter values of Y:")
for i in range(n):
    Y.append(float(input()))

# Calculations
sumX = sum(X)
sumY = sum(Y)
sumXY = sum(X[i] * Y[i] for i in range(n))
sumX2 = sum(x * x for x in X)

# Slope (b)
b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX ** 2)

# Intercept (a)
a = (sumY - b * sumX) / n

print("\n--- Linear Regression Equation ---")
print(f"Y = {a:.4f} + {b:.4f}X")

# Prediction
x_new = float(input("\nEnter value of X to predict Y: "))
y_pred = a + b * x_new

print(f"Predicted Y = {y_pred:.4f}")