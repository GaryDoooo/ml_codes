import yfinance as yf
import pandas as pd

# Download historical daily data for GLD
df = yf.download("GLD", period="max", interval="1d")

# Calculate daily percentage change on 'Close' price
df['Daily Change Rate Percent'] = df['Close'].pct_change() * 100

# Resample data weekly (using week ending on Sunday by default)
weekly = df['Close'].resample('W').last()

# Calculate weekly percentage change rate
weekly_change = weekly.pct_change() * 100
weekly_change = weekly_change.rename("Weekly Change Rate Percent")

# Join weekly change back to the original DataFrame aligned by date of week end
df = df.join(weekly_change, how='left')

# Optionally, add columns for start and end of the week for each date
df['Week Start'] = df.index.to_period('W').start_time
df['Week End'] = df.index.to_period('W').end_time

# Save all data including daily and weekly change rates to CSV
df.to_csv("GLD_daily_and_weekly_change.csv")

# Print the first few rows for verification
print(df.head(15))

