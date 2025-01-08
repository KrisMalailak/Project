import pandas as pd

# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")

# Menampilkan 5 baris pertama dari dataframe
print(customers_df.head())  # Menampilkan 5 baris pertama

# Menampilkan informasi tentang dataframe
customers_df.info()   # Menampilakn informasi kolom, tipe data, dan jumlah nilai non-null

# Menghitung jumlah nilai NaN di dalam dataframe
print("\nJumlah nilai NaN di tiap kolom:")
print(customers_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom 

# Menghitung jumlah duplikasi sebelum penghapusan
print("\nJumlah duplikasi sebelum penghapusan: ", customers_df.duplicated().sum())   # Menghitung jumlah duplikasi baris

# Menghapus duplikasi
customers_df.drop_duplicates(inplace=True)  # Menghapus baris yang duplikat

# Menghitung jumlah duplikasi setelah penghapusan
print("\nJumlah duplikasi setelah penghapusan: ", customers_df.duplicated().sum())   # Mengecek apakah duplikasi sudah dihapus

# Menampilkan statistik deskriptif dari dataframe
print("\nStatistik deskriptif dari dataframe:")
print(customers_df.describe())    # Menampilkan statistik deskriptif dari dataframe

# Mengisi nilai NaN pada kolom gender dengan "Prefer not to say"
customers_df.fillna(value="Prefer not to say", inplace=True)  # Mengganti nilai NaN di kolom 'gender'

# Menghitung dan menampilkan frekuensi nilai pada kolom 'gender'
print("\nFrekuensi nilai pada kolom 'gender':")
print(customers_df.gender.value_counts())     # Menghitung dan menampilkan frekuensi nilai di kolom 'gender'

# Memeriksa kembali apakah masih ada nilai NaN setelah pengisian
print("\nJumlah nilai NaN setelah pengisian:")
print(customers_df.isna().sum())   # Mengecek apakah masih ada nilai NaN


# Menampilkan baris pelanggan yang memiliki umur tertinggi
print("\nBaris pelanggan dengan umur tertinggi:")
print(customers_df[customers_df.age == customers_df.age.max()])  # Menampilkan baris dengan umur maksimal


# Mengganti nilai umur maksimum dengan 70
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)  # Mengganti nilai umur maksimal dengan 70


# Menampilkan kembali baris pelanggan yang memiliki umur tertinggi setelah penggantian
print("\nBaris pelanggan dengan umur tertinggi setelah penggantian umur maksimal:")
print(customers_df[customers_df.age == customers_df.age.max()])   # Menampilkan baris setelah perubahan umur maksimal


# Menampilkan kembali statistik deskriptif untuk melihat perubahan
print("\nStatistik deskriptif setelah mengganti umur maksimum:")
print(customers_df.describe())   # Menampilkan statistik deskriptif setelah perubahan












# Contoh ke-2 #


# import pandas as pd


# # Membaca file CSV dari URL
# customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")


# # Menampilkan 5 baris pertama dari dataframe
# print(customers_df.head())  # Menampilkan 5 baris pertama


# # Menampilkan informasi tentang dataframe
# customers_df.info()   # Menampilakn informasi kolom, tipe data, dan jumlah nilai non-null


# # Menghitung jumlah nilai NaN di dalam dataframe
# print("\nJumlah nilai NaN di tiap kolom:")
# print(customers_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom 


# # Menghitung jumlah duplikasi sebelum penghapusan
# print("\nJumlah duplikasi sebelum penghapusan: ", customers_df.duplicated().sum())   # Menghitung jumlah duplikasi baris


# # Menghapus duplikasi
# customers_df.drop_duplicates(inplace=True)  # Menghapus baris yang duplikat


# # Menghitung jumlah duplikasi setelah penghapusan
# print("\nJumlah duplikasi setelah penghapusan: ", customers_df.duplicated().sum())   # Mengecek apakah duplikasi sudah dihapus


# # Menampilkan statistik deskriptif dari dataframe
# print("\nStatistik deskriptif dari dataframe:")
# print(customers_df.describe())    # Menampilkan statistik deskriptif dari dataframe


# # Menampilkan baris-baris di mana kolom 'gender' memiliki nilai NaN
# print("\nBaris di mana kolom 'gender' memiliki nilai NaN:")
# print(customers_df.isna().sum())   # Mengecek apakah masih ada nilai NaN


# # Menghitung dan menampilkan frekuensi nilai pada kolom 'gender'
# print("\nFrekuensi nilai pada kolom 'gender':")
# print(customers_df.gender.value_counts())     # Menghitung dan menampilkan frekuensi nilai di kolom 'gender'



















