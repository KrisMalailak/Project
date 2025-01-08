import yfinance as yf
import matplotlib.pyplot as plt


# Mendapatkan data saham BBCA menggunakan yfinance
df = yf.download('BBCA.JK', start="2022-02-14", end="2023-02-14")


# Plot data
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['Close'], label='Close', color='red')
plt.plot(df.index, df['Open'], label='open', color='blue')
plt.title('BBCA Stock Price', size=20)
# plt.xlabel('Date', size=15)
# plt.ylabel('Price(IDR)', size=15)
plt.legend()
plt.show()