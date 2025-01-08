import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Mengambil data saham BBCA menggunakan yfinance
ticker = "BBCA.JK"
df = yf.download(ticker, start="2022-02-14", end="2023-02-14")

# Mengecek apakah data berhasil diambil
if df.empty:
    print("Data tidak ditemukan atau kosong.")
else:
    # Menyiapkan data untuk boxplot
    df_boxplot = df[["Open", "High", "Low", "Close", "Adj Close"]]

    # Membuat boxplot menggunakan seaborn
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_boxplot, palette="coolwarm")

    # Menambahkan grid pada grafik agar lebih mudah dibaca
    plt.grid(True)

    # Menambahkan label dan judul
    plt.ylabel('Price', size=15)
    plt.xlabel('Price Type', size=15)
    plt.title('BBCA Stock Price Distribution (Feb 2022 - Feb 2023)', size=16)

    # Menampilkan grafik
    plt.show()
