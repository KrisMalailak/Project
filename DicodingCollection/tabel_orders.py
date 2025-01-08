import pandas as pd

# Membaca file CSV dari URL
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")

# Menampilkan 5 baris pertama dari dataframe
print(orders_df.head())  # Menggunakan print untuk menampilkan output


# Menampilkan informasi tentang dataframe
orders_df.info() # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null


# Menampilkan jumlah duplikasi
print("Jumlah duplikasi: ", orders_df.duplicated().sum()) # Menampilkan jumlah baris yang duplikat


# Menampilkan statistik deskriptif
print(orders_df.describe())  # Menampilkan statistik deskriptif mean, standar deviasi, nilai minimum dan maksimum


# Mentukan kolom yang akan dikonversi
datetime_columns = ["order_date", "delivery_date"]


# Mengonversi kolom ke dalam format datetime
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column])  # Mengonversi kolom menjadi datetime


# Menampilkan informasi tentang dataframe orders_df setelah konversi
print("\nInformasi orders_df setelah konversi kolom:")
orders_df.info()   # Menampilkan informasi tentang orders_df setelah konversi