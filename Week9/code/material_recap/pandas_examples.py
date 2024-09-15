import pandas as pd

# 1. DataFrame: A two-dimensional labeled data structure, similar to a table in a relational database or Excel spreadsheet.
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)
print("DataFrame Example:")
print(df)
print("\n")

# 2. Series: A one-dimensional labeled array capable of holding any data type.
# Creating a Series from a list
s = pd.Series([10, 20, 30, 40, 50], name="Numbers")
print("Series Example:")
print(s)
print("\n")

# 3. Data Manipulation: Functions for filtering, merging, grouping, aggregating, and transforming data.

# Filtering Example
# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("Filtered Data (Age > 30):")
print(filtered_df)
print("\n")

# Merging Example
# Create two DataFrames and merge them on a common column
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Salary': [50000, 60000, 70000]})
merged_df = pd.merge(df1, df2, on='ID')
print("Merged DataFrame:")
print(merged_df)
print("\n")

# Grouping and Aggregating Example
# Group by 'City' and calculate the mean Age for each group
grouped = df.groupby('City')['Age'].mean()
print("Grouped and Aggregated Data (Mean Age by City):")
print(grouped)
print("\n")

# 4. Handling Missing Data: Tools to handle missing values with ease.

# Creating a DataFrame with missing values
data_with_missing = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, None, 35],
    'City': ['New York', 'San Francisco', None]
}
df_missing = pd.DataFrame(data_with_missing)
print("Original DataFrame with Missing Values:")
print(df_missing)
print("\n")

# Fill missing values with a default value
df_filled = df_missing.fillna("Unknown")
print("DataFrame after Filling Missing Values:")
print(df_filled)
print("\n")

# Drop rows with any missing values
df_dropped = df_missing.dropna()
print("DataFrame after Dropping Rows with Missing Values:")
print(df_dropped)
print("\n")

# 5. Read/Write: Functions to read from and write to different file formats like CSV, Excel, JSON, SQL, and more.

# For reading and writing data from CSV files
# Assuming 'data.csv' is an existing CSV file, uncomment the line below to read it
# df_from_csv = pd.read_csv('data.csv')
# print(df_from_csv.head())

# For demonstration, we can write the DataFrame to a CSV file
# Save DataFrame to a CSV file without row indices
df.to_csv('output.csv', index=False)
print("DataFrame written to 'output.csv'.")

# For reading and writing data from Excel files
# Assuming 'data.xlsx' is an existing Excel file, uncomment the line below to read it
# df_from_excel = pd.read_excel('data.xlsx')
# print(df_from_excel.head())

# Writing the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)  # Save DataFrame to an Excel file
print("DataFrame written to 'output.xlsx'.")

# For reading and writing data from JSON files
# Assuming 'data.json' is an existing JSON file, uncomment the line below to read it
# df_from_json = pd.read_json('data.json')
# print(df_from_json.head())

# Writing the DataFrame to a JSON file
# Save DataFrame to a JSON file
df.to_json('output.json', orient='records', lines=True)
print("DataFrame written to 'output.json'.")
