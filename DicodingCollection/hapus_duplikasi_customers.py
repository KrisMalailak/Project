import pandas as pd

# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")

# Menampilkan 5 baris pertama dari dataframe
print(customers_df.head())  # Menampilkan 5 baris pertama

# Menampilkan informasi tentang dataframe
customers_df.info()  # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null

# Menghitung jumlah nilai NaN di dalam dataframe
print("\nJumlah nilai NaN di tiap kolom:")
print(customers_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom

# Menghitung jumlah duplikasi sebelum penghapusan   
print("\nJumlah duplikasi sebelum penghapusan: ", customers_df.duplicated().sum())  # Menghitung jumlah duplikasi baris

# Menghapus duplikasi
customers_df.drop_duplicates(inplace=True)  # Menghapus baris yang duplikat

# Menghitung jumlah duplikasi setelah penghapusan
print("\nJumlah duplikasi setelah penghapusan: ", customers_df.duplicated().sum())  # Mengecek apakah duplikasi sudah dihapus

# Menampilkan statistik deskriptif dari dataframe
print("\nStatistik deskriptif dari dataframe:")
print(customers_df.describe())  # Menampilkan statistik deskriptif dari dataframe


# Menampilkan baris-baris di kolom  'gender' memiliki nilai NaN
print("\nBaris dimana kolom 'gender' memiliki nilai NaN:")
print(customers_df[customers_df.gender.isna()])   # Menampilkan baris dengan 'gender' NaN


# Menghitung dan menampilkan frekuensi nilai kolom 'gender'
print("\nFrekuensi nilai pada kolom 'gender':")
print(customers_df.gender.value_counts())  # Menghitung dan menampilkan frekuensi nilai di kolom 'gender'




