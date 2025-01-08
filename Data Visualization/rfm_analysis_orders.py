import pandas as pd


# Membaca file CSV dari URL
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")


# Menampilkan 5 baris pertama dari dataframe
print(orders_df.head())   # Menampilkan 5 baris pertama


# Menampilkan informasi tentang dataframe
orders_df.info()      # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null


# Menampilkan jumlah duplikasi
print("Jumlah duplikasi:", orders_df.duplicated().sum())  # Menampilkan jumlah baris yang duplikat


# Menampilkan statistik deskriptif 
print(orders_df.describe())       # Menampilkan statistik deskriptif mean, standar deviasi, nilai minimum dan maksimum


# Menentukan kolom yang akan dikonversi
datetime_columns = ["order_date", "delivery_date"]


# Mengonversi kolom ke dalam format datatime
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column])    # Mengonversi kolom menjadi datetime


# Menampilkan informasi tentang daraframe orders_df setelah konversi
print("\nInformasi orders_df setelah konversi kolom:")
orders_df.info()     # Menampilkan informasi tentang orders_df setelah konversi


# Menghitung selisih waktu antara delivery_date dan order_date
delivery_time = orders_df["delivery_date"] - orders_df["order_date"]


# Mengonversi selisih waktu menjadi detik, kemudian hari (86400 detik dalam sehari)
delivery_time = delivery_time.apply(lambda x: x.total_seconds() if pd.notnull(x) else 0)     # Mengatasi nilai null
orders_df["delivery_time"] = round(delivery_time / 86400)     # Mengonversi ke hari dan menambahkannya ke dataframe


# Menampilkan 5 baris pertaman dengan kolom baru "delivery_time"
print("\n5 baris pertama setelah menambahkan kolom 'delivery_time':")
print(orders_df.loc[[712, 716, 855, 35, 645], ['order_id', 'customer_id', 'payment', 'order_date', 'delivery_date', 'delivery_time']])


# Menampilkan statistik deskriptif untuk semua kolom
print("\nStatistik deskriptif untuk semua kolom:")
print(orders_df.describe(include="all"))       # Menampilkan statistik deskriptif untuk semua kolom, termasuk yang non-numerik


# RFM Analysis
rfm_df = orders_df.groupby(by="customer_id", as_index=False).agg({
    "order_date" : "max",                 # Mengambil tanggal order terakhir
    "order_id"   : "nunique",             # Menghitung jumlah order
    "payment"    : "sum"                  # Menghitung jumlah revenue yang dihasilkan (menggunakan payment)
})


# Mengganti nama kolom
rfm_df.columns = ["customer_id", "max_order_timestamp", "freque", "monetary"]


# Menghitung kapan terakhir pelanggan melakukan transaksi (hari)
rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
recent_date = orders_df["order_date"].dt.date.max()
rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)


# Menghapus kolom 'max_order_timestamp' yang sudah tidak diperlukan
rfm_df.drop("max_order_timestamp", axis=1, inplace=True)


# Menampilkan 5 baris pertama dari dataframe RFM
print("\n5 baris pertama dari RFM dataframe:")
print(rfm_df.head()) 