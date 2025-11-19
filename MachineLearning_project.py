import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from datetime import datetime
import os

API_KEY = ''
SYMBOL = 'AAPL' 
API_URL = ''

params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': SYMBOL,
    'outputsize': 'ull',
    'apikey': API_KEY
}

response = requests.get(API_URL, params=params)
data = response.json()

if "Time Series (Daily)" not in data:
    print("Gagal mengambil data. Periksa API key atau limit API.")
    exit()

df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
df = df.rename(columns={
    '1. open': 'open',
    '2. high': 'high',
    '3. low': 'low',
    '4. close': 'close',
    '5. adjusted close': 'adj_close',
    '6. volume': 'volume',
})
df = df.astype(float)
df['date'] = pd.to_datetime(df.index)
df = df.sort_values('date')

df['day_number'] = (df['date'] - df['date'].min()).dt.days
X = df[['day_number']]  
y = df['close']        

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Harga Sebenarnya')
plt.plot(X_test, y_pred, color='red', label='Prediksi')
plt.xlabel('Hari ke-n')
plt.ylabel('Harga Penutupan (USD)')
plt.title(f'Prediksi Harga Saham {SYMBOL} dengan Linear Regression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
