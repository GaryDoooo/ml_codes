import pandas as pd

# Read the data from the text file (assuming comma-separated values)
# Replace 'your_data.txt' with your actual filename
df = pd.read_csv("tsla.csv", header=None,
                 names=['Date', 'Close', 'High', 'Low', 'Open', 'Volume','Change'])

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Resample to weekly frequency taking last close price of each week
weekly_close = df['Close'].resample('W').last()

# Calculate weekly percentage change
weekly_change = weekly_close.pct_change() * 100

# Combine into a DataFrame
weekly_df = pd.DataFrame({
    'Weekly Close': weekly_close,
    'Weekly Change Rate Percent': weekly_change
})

#  print(weekly_df)

weekly_df.to_csv('tsla_wk.csv')
