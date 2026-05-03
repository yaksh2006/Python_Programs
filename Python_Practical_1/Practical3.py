import pandas as pd
import numpy as np

# Sample dataset with missing values
data = {
    'Age': [25, np.nan, 37, 35, np.nan],
    'Salary': [50000, 60000, np.nan, 80000, 75000, np.nan],
    'City': ['Delhi', 'Mumbai', np.nan, 'Delhi', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)

print("Original Data:\n", df)
print("\nMissing Values Count:\n", df.isnull().sum())

# -------------------------------
# 1. Mean Imputation (Numerical)
# -------------------------------
df_mean = df.copy()
df_mean['Age'].fillna(df_mean['Age'].mean(), inplace=True)
df_mean['Salary'].fillna(df_mean['Salary'].mean(), inplace=True)

print("\nAfter Mean Imputation:\n", df_mean)

# -------------------------------
# 2. Median Imputation (Numerical)
# -------------------------------
df_median = df.copy()
df_median['Age'].fillna(df_median['Age'].median(), inplace=True)
df_median['Salary'].fillna(df_median['Salary'].median(), inplace=True)

print("\nAfter Median Imputation:\n", df_median)

# -------------------------------
# 3. Mode Imputation (Categorical)
# -------------------------------
df_mode = df.copy()
df_mode['City'].fillna(df_mode['City'].mode()[0], inplace=True)

print("\nAfter Mode Imputation:\n", df_mode)

# -------------------------------
# 4. Forward Fill (ffill)
# -------------------------------
df_ffill = df.copy()
df_ffill.fillna(method='ffill', inplace=True)

print("\nAfter Forward Fill:\n", df_ffill)

# -------------------------------
# 5. Backward Fill (bfill)
# -------------------------------
df_bfill = df.copy()
df_bfill.fillna(method='bfill', inplace=True)

print("\nAfter Backward Fill:\n", df_bfill)

# -------------------------------
# 6. All-in-One Imputation Function
# -------------------------------
def impute_data(df):
    df = df.copy()

    # Numerical columns
    num_cols = df.select_dtypes(include=np.number).columns
    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)

    # Categorical columns
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df

df_final = impute_data(df)

print("\nFinal Cleaned Data:\n", df_final)