import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Download Ethereum data from Yahoo Finance
eth = yf.download('ETH-USD', start='2022-01-01', end='2022-03-24')

# Calculate daily returns
eth['returns'] = eth['Close'].pct_change()

# Drop any rows with missing data
eth.dropna(inplace=True)

# Split the data into features and target
X = eth[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].values
y = eth['returns'].values

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the linear regression model
model = LinearRegression()
model.fit(X_scaled, y)

# Save the scaler and model
joblib.dump(scaler, 'eth_scaler.pkl')
joblib.dump(model, 'eth_model.pkl')
