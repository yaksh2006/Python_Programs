import pandas as pd

# Create dataset
data = {
    'Age': [20, 25, 30],
    'Salary': [20000, 50000, 100000]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Min-Max Normalization
df_minmax = df.copy()

df_minmax['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
df_minmax['Salary'] = (df['Salary'] - df['Salary'].min()) / (df['Salary'].max() - df['Salary'].min())

print("\nMin-Max Normalized Data:\n", df_minmax)