import yfinance as yf

# Download maximum available daily price history for GLD
df = yf.download("GLD", period="max", interval="1d")

# Print first few rows
print(df.head())

# Save to CSV
df.to_csv("GLD_daily_history.csv")
