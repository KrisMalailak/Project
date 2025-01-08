# import pandas as pd


# # Membaca file CSV dari URL
# product_df =pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")


# # Menampilkan 5 baris pertama dari dataframe
# print(product_df.head())  # Menggunkan print untuk menampilkan output


# # Menampilkan informasi tentang dataframe
# product_df.info() # Menampilkan informasi kolom, tipe dat, dan jumlah nilai non-null


# # Menghitung jumlah duplikasi
# print("Jumlah duplikasi: ", product_df.duplicated().sum())


# # Menampilakan deskripsi dari dataframe
# print(product_df.describe())   # Menampilkan statistik deskriptif dari dataframe




























import pandas as pd

# Membaca file CSV dari URL
product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")

# Menampilkan 5 baris pertama dari dataframe
print(product_df.head())  # Menggunakan print untuk menampilkan output

# Menampilkan informasi tentang dataframe
product_df.info()  # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null

# Menghitung jumlah duplikasi sebelum penghapusan
print("Jumlah duplikasi sebelum penghapusan: ", product_df.duplicated().sum())

# Menghapus duplikasi
product_df.drop_duplicates(inplace=True)  # Menghapus baris yang duplikat

# Menghitung jumlah duplikasi setelah penghapusan
print("Jumlah duplikasi setelah penghapusan: ", product_df.duplicated().sum())  # Mengecek apakah duplikasi sudah dihapus

# Menampilkan deskripsi dari dataframe
print(product_df.describe())  # Menampilkan statistik deskriptif dari dataframe























