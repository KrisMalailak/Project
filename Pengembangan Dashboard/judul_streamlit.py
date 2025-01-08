import pandas as pd
import streamlit as st
from babel.numbers import format_currency
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='dark')

# Menampilkan header
st.header('Dicoding Collection Dashboard :sparkles:')

# Membaca file CSV dari URL
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")

# Menampilkan 5 baris pertama dari dataframe
st.write("5 Baris Pertama dari Dataframe:")
st.write(orders_df.head())

# Menampilkan informasi tentang dataframe
st.write("Informasi Dataframe:")
orders_info = orders_df.info()
st.text(orders_info)

# Menampilkan jumlah duplikasi
duplicate_count = orders_df.duplicated().sum()
st.write("Jumlah duplikasi: ", duplicate_count)

# Menampilkan statistik deskriptif
st.write("Statistik Deskriptif:")
st.write(orders_df.describe())

# Menentukan kolom yang akan dikonversi
datetime_columns = ["order_date", "delivery_date"]

for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column])

# Menghitung waktu pengiriman
delivery_time = orders_df["delivery_date"] - orders_df["order_date"]
orders_df["delivery_time"] = round(delivery_time.dt.total_seconds() / 86400)

# Mengambil nilai minimum dan maksimum dari order_date
min_date = orders_df["order_date"].min()
max_date = orders_df["order_date"].max()

# Sidebar untuk rentang waktu
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    start_date, end_date = st.date_input('Rentang Waktu', min_value=min_date, max_value=max_date, value=[min_date, max_date])

# Menyaring DataFrame berdasarkan rentang waktu yang dipilih
main_df = orders_df[(orders_df["order_date"] >= pd.to_datetime(start_date)) & 
                    (orders_df["order_date"] <= pd.to_datetime(end_date))]

# Fungsi-fungsi tambahan
def create_daily_orders_df(df):
    daily_orders_df = df.resample('D', on='order_date').agg({
        "order_id": "nunique",
        "payment": "sum"
    })
    daily_orders_df.rename(columns={"order_id": "order_count", "payment": "revenue"}, inplace=True)
    return daily_orders_df.reset_index()

def create_sum_order_items_df(df):
    return df.groupby("product_id").agg({
        "quantity": "sum",
        "payment": "sum"
    }).reset_index()

def create_bygender_df(df):
    return df.groupby("gender")["order_id"].count().reset_index()

def create_byage_df(df):
    return df.groupby("age")["order_id"].count().reset_index()

def create_bystate_df(df):
    return df.groupby("state")["order_id"].count().reset_index()

def create_rfm_df(df):
    now = pd.Timestamp.now()
    rfm_df = df.groupby("customer_id").agg({
        "order_date": lambda x: (now - x.max()).days,
        "order_id": "count",
        "payment": "sum"
    })
    rfm_df.columns = ["Recency", "Frequency", "Monetary"]
    return rfm_df.reset_index()

# Menggunakan fungsi tambahan pada data yang telah difilter
daily_orders_df = create_daily_orders_df(main_df)
sum_order_items_df = create_sum_order_items_df(main_df)
bygender_df = create_bygender_df(main_df)
byage_df = create_byage_df(main_df)
bystate_df = create_bystate_df(main_df)
rfm_df = create_rfm_df(main_df)

# Menampilkan data hasil pengolahan
st.write("Data Pesanan Harian:")
st.write(daily_orders_df.head())

st.write("Jumlah Item Pesanan:")
st.write(sum_order_items_df.head())

st.write("Pesanan Berdasarkan Jenis Kelamin:")
st.write(bygender_df)

st.write("Pesanan Berdasarkan Usia:")
st.write(byage_df)

st.write("Pesanan Berdasarkan Negara Bagian:")
st.write(bystate_df)

st.write("Analisis RFM Pelanggan:")
st.write(rfm_df.head())