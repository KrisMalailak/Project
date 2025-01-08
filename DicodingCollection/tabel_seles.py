import pandas as pd

# Membaca file CSV dari URL
sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")

# Menampilkan 5 baris pertama dari dataframe
print(sales_df.head())  # Menggunakan print untuk menampilkan output

# Menampilkan informasi tentang dataframe
sales_df.info()  # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null

# Menghitung jumlah nilai NaN di dalam dataframe
print("\nJumlah nilai NaN di tiap kolom:")
print(sales_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom 

# Menghitung jumlah duplikasi di dalam dataframe
print("\nJumlah duplikasi:", sales_df.duplicated().sum())

# Menampilkan statistik deskriptif dari dataframe
print("\nStatistik deskriptif dari dataframe:")
print(sales_df.describe())  # Menampilkan statistik deskriptif dari dataframe

# Menampilkan baris di mana kolom 'total_price' memiliki nilai NaN
print("\nBaris dengan nilai NaN di kolom 'total_price':")
print(sales_df[sales_df.total_price.isna()])  # Menampilkan baris dengan nilai NaN di kolom 'total_price'


# Menghitung ulang kolom 'total_price' sebagai hasil perkalian 'price_per_unit' dan 'quantity'
sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"]


# Menampilkan baris di mana kolom 'total_price' memiliki nilai NaN setelah perhitungan
print("\nBaris dengan nilai NaN di kolom 'total_price' setelah perhitungan:")
print(sales_df[sales_df.total_price.isna()])  # Menampilkan baris dengan nilai NaN di kolom 'total_price' setelah perhitungan


# Menghitung jumlah nilai NaN di dalam dataframe setelah perhitungan 'total_price'
print("\nJumlah nilai NaN di tiap kolom setelah perhitungan total_price:")
print(sales_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom setelah perhitungan 'total_price'

















































































































































































