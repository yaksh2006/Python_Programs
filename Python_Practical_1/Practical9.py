import pandas as pd

# -----------------------------
# Step 1: Create Sample Data
# -----------------------------
data = {
    'ID': [1, 2, 3, 4, 5, 5],
    'Name': ['Aman', 'Riya', 'Karan', 'Sneha', 'Rahul', 'Rahul'],
    'Age': [20, 21, None, 22, 20, 20],
    'Marks': [85, 90, 78, None, 76, 76]
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("students.csv", index=False)

# -----------------------------
# 1️⃣ Reading Data
# -----------------------------
df = pd.read_csv("students.csv")
print("Original Data:\n", df)

# -----------------------------
# 2️⃣ Viewing Data
# -----------------------------
print("\nFirst 5 rows:\n", df.head())
print("\nInfo:\n")
print(df.info())
print("\nStatistical Summary:\n", df.describe())

# -----------------------------
# 3️⃣ Handling Missing Values
# -----------------------------
print("\nMissing Values:\n", df.isnull().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Marks'].fillna(0, inplace=True)

print("\nAfter Handling Missing Values:\n", df)

# -----------------------------
# 4️⃣ Removing Duplicates
# -----------------------------
df = df.drop_duplicates()
print("\nAfter Removing Duplicates:\n", df)

# -----------------------------
# 5️⃣ Renaming Columns
# -----------------------------
df.rename(columns={'Marks': 'Score'}, inplace=True)
print("\nAfter Renaming Column:\n", df)

# -----------------------------
# 6️⃣ Changing Data Type
# -----------------------------
df['Age'] = df['Age'].astype(int)
print("\nData Types:\n", df.dtypes)

# -----------------------------
# 7️⃣ Filtering Data
# -----------------------------
filtered = df[df['Score'] > 80]
print("\nStudents with Score > 80:\n", filtered)

# -----------------------------
# 8️⃣ Sorting Data
# -----------------------------
sorted_df = df.sort_values(by='Score', ascending=False)
print("\nSorted Data:\n", sorted_df)

# -----------------------------
# 9️⃣ Merging Two DataFrames
# -----------------------------
data2 = {
    'ID': [1, 2, 3, 4, 5],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Pune']
}

df2 = pd.DataFrame(data2)

merged = pd.merge(df, df2, on='ID')
print("\nMerged Data:\n", merged)