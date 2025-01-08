import pandas as pd

# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")

# Menampilkan 5 baris pertama dari dataframe
print(customers_df.head())


# Menampilkan informasi tentang dataframe
customers_df.info()


# Menghitung jumlah nilai yang hilang di setiap kolom
missing_values = customers_df.isna().sum()


# Menampilkan jumlah nilai yang hilang (missing values)
print("\nJumlah nilai yang hilang di setiap kolom:")
print(missing_values)


# Menghitung jumlah duplikasi dalam dataframe
duplicates_count = customers_df.duplicated().sum()


# Menam[ilkan jumlah duplikasi
print("\nJumlah duplikasi: ",duplicates_count)


# Menampilkan statistik deskriptif dari dataframe
print("\nStatistik deskriptif dari dataframe:")
print(customers_df.describe())
