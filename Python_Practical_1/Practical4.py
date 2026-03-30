import pandas as pd

# Given data
marks = [45, 50, 48, 52, 49, 1000]

# Create DataFrame
df = pd.DataFrame(marks, columns=['Marks'])

print("Original Data:\n", df)

# -----------------------------
# Step 1: Calculate Quartiles
# -----------------------------
Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)

# Step 2: IQR
IQR = Q3 - Q1

# Step 3: Define limits
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# -----------------------------
# Step 4: Detect Outliers
# -----------------------------
outliers = df[(df['Marks'] < lower_bound) | (df['Marks'] > upper_bound)]

print("\nOutliers:\n", outliers)

# -----------------------------
# Step 5: Remove Outliers
# -----------------------------
df_clean = df[(df['Marks'] >= lower_bound) & (df['Marks'] <= upper_bound)]

print("\nData after removing outliers:\n", df_clean)