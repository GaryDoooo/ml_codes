import pandas as pd

# Load the CSV file
df = pd.read_csv("GLD_daily_history.csv", skiprows=2)  # Skip first 2 non-data header rows

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculate daily change rate based on 'Close' column
df['Daily Change Rate'] = df['Close'].pct_change()

# Optionally multiply by 100 for percentage
df['Daily Change Rate Percent'] = df['Daily Change Rate'] * 100

# Save the updated dataframe back to CSV
df.to_csv("GLD_daily_history_with_change.csv", index=False)

# Print the first few rows to verify
print(df.head())

