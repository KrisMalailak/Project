import yfinance as yf
import matplotlib.pyplot as plt

# Mendapatkan data saham BBCA menggunakan yfinance
ticker = "BBCA.JK"
df = yf.download(ticker, start="2022-02-14", end="2023-02-14")

# Cek apakah data berhasil diambil
if df.empty:
    print("Data tidak ditemukan atau kosong.")
else:
    # Plot data
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['Close'], color='red')
    plt.xlabel('Date', size=15)
    plt.ylabel('Price', size=15)
    plt.title('BBCA Stock Prices')
    plt.show()