# import pandas as pd


# # Membaca file CSV dari URL
# orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")


# # Menampilkan 5 baris pertama dari dataframe
# print(orders_df.head())  # Menampilkan 5 baris pertama


# # Menampilkan informasi tentang dataframe
# orders_df.info()   # Menampilkan informasi kolom, tipe data, dan jumlah nilai noll


# # Menampilkan jumlah duplikasi
# print("Jumlah duplikasi: ", orders_df.duplicated().sum())  # Menampilkan jumlah baris yang duplikat


# # Menampilkan statistik deskriptif
# print(orders_df.describe())  # Menampilkan statistik deskriptif mean, standar deviasi, nilai minimum dan maksimum


# # Mentukan kolom yang akan dikonversi
# datetime_columns = ["order_date", "delivery_date"]


# # Mengonversi kolom ke dalam format datetime
# for column in datetime_columns:
#     orders_df[column] = pd.to_datetime(orders_df[column], errors='coerce') # mengonversi kolom menjadi datetime, menangani error


# # Menampilkan informasi tentang dataframe orders_df setelah konversi
# print("\nInformasi orders_df setelah konversi kolom:")
# orders_df.info()   # Menampilkan informasi tentang orders_df setelah konversi


# # Menghitung selisih waktu antar delivery_date dan order_date
# delivery_time = orders_df["delivery_date"] - orders_df["order_date"]


# # mengonversi selisih waktu menjadi detik, kemudian hari (86400 detik dalam sehari)
# delivery_time = delivery_time.apply(lambda x: x.total_seconds() if pd.notnull(x) else 0)
# orders_df["delivery_time"] = round(delivery_time / 86400)   # Mengonversi ke hari dan menambahkannya ke dataframe


# # Menampilkan 5 baris pertama dengan kolom baru "delivery_time"
# print("\n5 baris pertama setelah menambahkan kolom 'delivery_time':")
# print(orders_df[['order_id', 'customer_id', 'payment', 'order_date', 'delivery_date', 'delivery_time']].head())  # Menampilkan 5 baris pertama


# # Menampilkan statistik deskriptif untuk semua kolom
# print("\nStatistik deskriptif untuk semua kolom:")
# print(orders_df.describe(include="all"))    # Menampilkan statistik deskriptif untuk semua kolom, termasuk yang non-numerik


# # Menambahkan kolom total_price jika tidak ada
# # Pastikan total_price ada, jika tidak ada gunakan contoh perhitungan dari kolom pembayaran dan jumlah
# if "total_price" not in orders_df.columns:
#     orders_df["total_price"] = orders_df["payment"]  # Misalnya, total_price diambil dari kolom payment


# # Menghitung data pesanan bulanan
# monthly_orders_df = orders_df.resample(rule='M', on='order_date').agg({
#     "order_id" : "nunique",      # Menghitung jumlah unik dari order_id
#     "total_price" : "sum"        # Menghitung total pendapatan 
# })


# # Menformat indeks sebagi string
# monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')


# # Mengubah index ke kolom 
# monthly_orders_df = monthly_orders_df.reset_index()


# # Mengganti nama kolom 
# monthly_orders_df.rename(columns={
#     "order_id" : "order_count",
#     "total_price" : "revenue"
# }, inplace=True)


# # Menampilkan hasil 
# print("\n5 baris pertama dari mothly_orders_df:")
# print(monthly_orders_df.head())






























































import pandas as pd

# Membaca file CSV dari URL
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")

# Menampilkan 5 baris pertama dari dataframe
print(orders_df.head())  # Menampilkan 5 baris pertama

# Menampilkan informasi tentang dataframe
orders_df.info()   # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null

# Menampilkan jumlah duplikasi
print("Jumlah duplikasi: ", orders_df.duplicated().sum())  # Menampilkan jumlah baris yang duplikat

# Menampilkan statistik deskriptif
print(orders_df.describe())  # Menampilkan statistik deskriptif mean, standar deviasi, nilai minimum dan maksimum

# Menentukan kolom yang akan dikonversi
datetime_columns = ["order_date", "delivery_date"]

# Mengonversi kolom ke dalam format datetime
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column], errors='coerce') # mengonversi kolom menjadi datetime, menangani error

# Menampilkan informasi tentang dataframe orders_df setelah konversi
print("\nInformasi orders_df setelah konversi kolom:")
orders_df.info()   # Menampilkan informasi tentang orders_df setelah konversi

# Menghitung selisih waktu antar delivery_date dan order_date
delivery_time = orders_df["delivery_date"] - orders_df["order_date"]

# Mengonversi selisih waktu menjadi detik, kemudian hari (86400 detik dalam sehari)
delivery_time = delivery_time.apply(lambda x: x.total_seconds() if pd.notnull(x) else 0)
orders_df["delivery_time"] = round(delivery_time / 86400)   # Mengonversi ke hari dan menambahkannya ke dataframe

# Menampilkan 5 baris pertama dengan kolom baru "delivery_time"
print("\n5 baris pertama setelah menambahkan kolom 'delivery_time':")
print(orders_df[['order_id', 'customer_id', 'payment', 'order_date', 'delivery_date', 'delivery_time']].head())  # Menampilkan 5 baris pertama

# Menampilkan statistik deskriptif untuk semua kolom
print("\nStatistik deskriptif untuk semua kolom:")
print(orders_df.describe(include="all"))    # Menampilkan statistik deskriptif untuk semua kolom, termasuk yang non-numerik

# Menambahkan kolom total_price jika tidak ada
if "total_price" not in orders_df.columns:
    orders_df["total_price"] = orders_df["payment"]  # Misalnya, total_price diambil dari kolom payment

# Menghitung data pesanan bulanan
monthly_orders_df = orders_df.resample(rule='M', on='order_date').agg({
    "order_id": "nunique",      # Menghitung jumlah unik dari order_id
    "total_price": "sum"        # Menghitung total pendapatan 
})

# Memformat indeks sebagai string
monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')

# Mengubah indeks ke kolom
monthly_orders_df = monthly_orders_df.reset_index()

# Mengganti nama kolom
monthly_orders_df.rename(columns={
    "order_id": "order_count",
    "total_price": "revenue"
}, inplace=True)

# Menampilkan hasil
print("\n5 baris pertama dari monthly_orders_df:")
print(monthly_orders_df.head())
