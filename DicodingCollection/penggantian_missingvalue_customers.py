import pandas as pd

# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")


# Menampilkan 5 baris pertama dari dataframe
print(customers_df.head())  # Menampilkan 5 baris pertama


# Menampilkan informasi tentang dataframe
print("\nJumlah nilai NaN di tiap kolom:")
print(customers_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom


# Menghitung jumlah duplikasi sebelum penghapusan
print("\nJumlah duplikasi sebelum penghapusan: ", customers_df.duplicated().sum())  # Menghitung jumlah duplikat baris


# Menampilkan statistik deskriptif dari dataframe
print("\nStatistik deskriptif dari dataframe:")
print(customers_df.describe())   # Menampilkan statistik deskriptif dari dataframe


# Menampilkan baris-baris di mana kolom 'gender' memiliki nilai NaN
print("\nBaris di mana kolom 'gender' memiliki nilai NaN:")
print(customers_df[customers_df.gender.isna()])    # Menampilkan baris dengan 'gender'NaN


# Mengisi nilai NaN di kolom 'gender' dengan 'prefer no to say'
customers_df.fillna(value="prefer no to say", inplace=True)    # Mengisi nilai NaN dengan 'Prefer not to say'


# Menampilkan kembali jumlah nilai NaN setelah diisi
print("\nJumlah nilai NaN setelah pengisian:")
print(customers_df.isna().sum())    # Mengecek apakah masih ada nilai NaN



# Menghitung dan menampilkan Frekuensi nilai pada kolom 'gender'
print("\nfrekuensi nilai pada kolom 'gender':")
print(customers_df.gender.value_counts())    # Menghitung dan menampilkan frekuensi nilai di kolom 'gender'













