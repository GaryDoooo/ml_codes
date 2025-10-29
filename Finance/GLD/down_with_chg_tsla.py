import yfinance as yf
import pandas as pd

# Download historical data for GLD
df = yf.download("TSLA", period="max", interval="1d")

# Calculate daily percentage change based on Close price
df['Daily Change Rate Percent'] = df['Close'].pct_change() * 100

# Save to a CSV file including the new column
df.to_csv("GLD_daily_history_with_change.csv")

# Print the first few rows to confirm
print(df.head())

