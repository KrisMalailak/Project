# import pandas as pd
# import streamlit as st

# # Membaca file CSV dari URL
# orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")

# # Menampilkan 5 baris pertama dari dataframe
# st.write("5 Baris Pertama dari Dataframe:")
# st.write(orders_df.head())  # Menampilkan 5 baris pertama

# # Menampilkan informasi tentang dataframe
# st.write("Informasi Dataframe:")
# orders_info = orders_df.info()  # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null
# st.text(orders_info)

# # Menampilkan jumlah duplikasi
# duplicate_count = orders_df.duplicated().sum()
# st.write("Jumlah duplikasi: ", duplicate_count)  # Menampilkan jumlah baris yang duplikat

# # Menampilkan statistik deskriptif
# st.write("Statistik Deskriptif:")
# st.write(orders_df.describe())  # Menampilkan statistik deskriptif mean, standar deviasi, nilai minimum dan maksimum

# # Menentukan kolom yang akan dikonversi
# datetime_columns = ["order_date", "delivery_date"]

# # Mengonversi kolom ke dalam format datetime
# for column in datetime_columns:
#     orders_df[column] = pd.to_datetime(orders_df[column])  # Mengonversi kolom menjadi datetime

# # Menampilkan informasi tentang dataframe orders_df setelah konversi
# st.write("\nInformasi orders_df setelah konversi kolom:")
# orders_info_after = orders_df.info()   # Menampilkan informasi tentang orders_df setelah konversi
# st.text(orders_info_after)

# # Menghitung selisih waktu antara delivery_date dan order_date
# delivery_time = orders_df["delivery_date"] - orders_df["order_date"]

# # Mengonversi selisih waktu menjadi detik, kemudian hari (86400 detik dalam sehari)
# delivery_time = delivery_time.apply(lambda x: x.total_seconds() if pd.notnull(x) else 0)  # Mengatasi nilai null
# orders_df["delivery_time"] = round(delivery_time / 86400)  # Mengonversi ke hari dan menambahkannya ke dataframe

# # Menampilkan 5 baris pertama dengan kolom baru "delivery_time"
# st.write("\n5 Baris Pertama setelah Menambahkan Kolom 'delivery_time':")
# st.write(orders_df.loc[[712, 716, 855, 35, 645], ['order_id', 'customer_id', 'payment', 'order_date', 'delivery_date', 'delivery_time']])

# # Menampilkan statistik deskriptif untuk semua kolom
# st.write("\nStatistik Deskriptif untuk Semua Kolom:")
# st.write(orders_df.describe(include="all"))  # Menampilkan statistik deskriptif untuk semua kolom, termasuk yang non-numerik

# # Mengambil nilai minimum dan maksimum dari order_date
# min_date = orders_df["order_date"].min()
# max_date = orders_df["order_date"].max()

# # Sidebar untuk rentang waktu
# with st.sidebar:
#     # Menambahkan logo perusahaan
#     st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
#     # Mengambil start_date & end_date dari date_input
#     start_date, end_date = st.date_input(
#         label='Rentang Waktu',
#         min_value=min_date,
#         max_value=max_date,
#         value=[min_date, max_date]
#     )

# # Menampilkan rentang waktu yang dipilih
# st.write("Rentang Waktu yang Dipilih:", start_date, "sampai", end_date)


















































import pandas as pd
import streamlit as st

# Membaca file CSV dari URL
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")

# Menampilkan 5 baris pertama dari dataframe
st.write("5 Baris Pertama dari Dataframe:")
st.write(orders_df.head())  # Menampilkan 5 baris pertama

# Menampilkan informasi tentang dataframe
st.write("Informasi Dataframe:")
orders_info = orders_df.info()  # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null
st.text(orders_info)

# Menampilkan jumlah duplikasi
duplicate_count = orders_df.duplicated().sum()
st.write("Jumlah duplikasi: ", duplicate_count)  # Menampilkan jumlah baris yang duplikat

# Menampilkan statistik deskriptif
st.write("Statistik Deskriptif:")
st.write(orders_df.describe())  # Menampilkan statistik deskriptif mean, standar deviasi, nilai minimum dan maksimum

# Menentukan kolom yang akan dikonversi
datetime_columns = ["order_date", "delivery_date"]

# Mengonversi kolom ke dalam format datetime
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column])  # Mengonversi kolom menjadi datetime

# Menampilkan informasi tentang dataframe orders_df setelah konversi
st.write("\nInformasi orders_df setelah konversi kolom:")
orders_info_after = orders_df.info()   # Menampilkan informasi tentang orders_df setelah konversi
st.text(orders_info_after)

# Menghitung selisih waktu antara delivery_date dan order_date
delivery_time = orders_df["delivery_date"] - orders_df["order_date"]

# Mengonversi selisih waktu menjadi detik, kemudian hari (86400 detik dalam sehari)
delivery_time = delivery_time.apply(lambda x: x.total_seconds() if pd.notnull(x) else 0)  # Mengatasi nilai null
orders_df["delivery_time"] = round(delivery_time / 86400)  # Mengonversi ke hari dan menambahkannya ke dataframe

# Menampilkan 5 baris pertama dengan kolom baru "delivery_time"
st.write("\n5 Baris Pertama setelah Menambahkan Kolom 'delivery_time':")
st.write(orders_df.loc[[712, 716, 855, 35, 645], ['order_id', 'customer_id', 'payment', 'order_date', 'delivery_date', 'delivery_time']])

# Menampilkan statistik deskriptif untuk semua kolom
st.write("\nStatistik Deskriptif untuk Semua Kolom:")
st.write(orders_df.describe(include="all"))  # Menampilkan statistik deskriptif untuk semua kolom, termasuk yang non-numerik

# Mengambil nilai minimum dan maksimum dari order_date
min_date = orders_df["order_date"].min()
max_date = orders_df["order_date"].max()

# Sidebar untuk rentang waktu
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Menampilkan rentang waktu yang dipilih
st.write("Rentang Waktu yang Dipilih:", start_date, "sampai", end_date)

# Menyaring DataFrame berdasarkan rentang waktu yang dipilih
main_df = orders_df[(orders_df["order_date"] >= pd.to_datetime(start_date)) & 
                    (orders_df["order_date"] <= pd.to_datetime(end_date))]

# Menampilkan data yang difilter
st.write("\nData dalam Rentang Waktu yang Dipilih:")
st.write(main_df)
