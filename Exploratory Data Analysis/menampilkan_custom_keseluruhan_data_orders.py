# Pilihan ke-2 tapi output nya menampilkan keseluruhan data dengan custom #

import pandas as pd

# Membaca file CSV dari URL
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")

# Menampilkan 5 baris pertama dari dataframe
print(orders_df.head())  # Menampilkan 5 baris pertama

# Menampilkan informasi tentang dataframe
orders_df.info()  # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null

# Menampilkan jumlah duplikasi
print("Jumlah duplikasi: ", orders_df.duplicated().sum())  # Menampilkan jumlah baris yang duplikat

# Menampilkan statistik deskriptif
print(orders_df.describe())  # Menampilkan statistik deskriptif mean, standar deviasi, nilai minimum dan maksimum

# Menentukan kolom yang akan dikonversi
datetime_columns = ["order_date", "delivery_date"]

# Mengonversi kolom ke dalam format datetime
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column])  # Mengonversi kolom menjadi datetime

# Menampilkan informasi tentang dataframe orders_df setelah konversi
print("\nInformasi orders_df setelah konversi kolom:")
orders_df.info()   # Menampilkan informasi tentang orders_df setelah konversi

# Menghitung selisih waktu antara delivery_date dan order_date
delivery_time = orders_df["delivery_date"] - orders_df["order_date"]

# Mengonversi selisih waktu menjadi detik, kemudian hari (86400 detik dalam sehari)
delivery_time = delivery_time.apply(lambda x: x.total_seconds() if pd.notnull(x) else 0)  # Mengatasi nilai null
orders_df["delivery_time"] = round(delivery_time / 86400)  # Mengonversi ke hari dan menambahkannya ke dataframe

# Menampilkan 5 baris pertama dengan kolom baru "delivery_time"
print("\n5 baris pertama setelah menambahkan kolom 'delivery_time':")
print(orders_df.loc[[712, 716, 855, 35, 645], ['order_id', 'customer_id', 'payment', 'order_date', 'delivery_date', 'delivery_time']])

# Membuat list customer_id dari orders_df
customer_id_in_orders_df = orders_df.customer_id.tolist()

# Membuat dataframe customers_df sesuai dengan gambar
customers_df = pd.DataFrame({
    'customer_id': [734, 282, 665, 564, 296],  # Sesuaikan dengan customer_id yang sesuai
    'customer_name': ['fulan 734', 'fulan 282', 'fulan 665', 'fulan 564', 'fulan 296'],
    'gender': ['Male', 'Female', 'Prefer not to say', 'Prefer not to say', 'Prefer not to say'],
    'age': [77, 59, 61, 34, 50],
    'home_address': [
        '145 Glover GroveSuite 556', '2634 Ward CrescentSuite 361', 
        '1713 Cormier RunSuite 980', '65 Schroeder WayApt. 552', 
        '831 Barton MallSuite 382'
    ],
    'zip_code': [3608, 4527, 2022, 4054, 7499],
    'city': ['Tylerburgh', 'Port Hannaburgh', 'Kiehnstad', 'North Marcusland', 'Port William'],
    'state': ['Western Australia', 'Australian Capital Territory', 
              'Australian Capital Territory', 'Northern Territory', 'Victoria'],
    'country': ['Australia', 'Australia', 'Australia', 'Australia', 'Australia']
})

# Menambahkan kolom status di customers_df
customers_df["status"] = customers_df["customer_id"].apply(lambda x: "Active" if x in customer_id_in_orders_df else "Non Active")

# Menampilkan data customers_df sesuai gambar
print("\nData customers_df setelah penambahan kolom 'status':")
print(customers_df)
