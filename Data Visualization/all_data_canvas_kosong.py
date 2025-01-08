import pandas as pd
import matplotlib.pyplot as plt  # Impor matplotlib untuk visualisasi

# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")

# Melakukan merge antara sales_df dan product_df berdasarkan product_id
sales_product_df = pd.merge(
    left=sales_df,
    right=product_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)

# Melakukan merge antara orders_df dan customers_df berdasarkan customer_id
orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)

# Menggabungkan hasil penggabungan sales_product_df dan orders_customers_df berdasarkan order_id
all_df = pd.merge(
    left=sales_product_df,
    right=orders_customers_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)

# Menampilkan 5 baris pertama dari dataframe hasil penggabungan
print("\n5 Baris pertama dari dataframe hasil penggabungan all_df:")
print(all_df.head())

# Mengelompokkan berdasarkan gender dan product_type, lalu melakukan agregasi quantity_x dan total_price
grouped_gender_product = all_df.groupby(by=["gender", "product_type"]).agg({
    "quantity_x": "sum",  # Menjumlahkan kuantitas per kelompok
    "total_price": "sum"  # Menjumlahkan total harga per kelompok
}).reset_index()

# Menampilkan hasil agregasi berdasarkan gender dan product_type
print("\nAgregasi berdasarkan gender dan product_type:")
print(grouped_gender_product)

# Membuat kolom 'age_group' berdasarkan kolom 'age'
bins = [0, 18, 35, 55, 100]  # Batas usia
labels = ["Youth", "Adults", "Middle-aged", "Seniors"]  # Tambahkan satu label lagi

# Menggunakan pd.cut untuk mengelompokkan berdasarkan umur
customers_df['age_group'] = pd.cut(customers_df['age'], bins=bins, labels=labels, right=False)

# Melakukan merge ulang untuk mendapatkan kolom age_group di all_df
orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)

all_df = pd.merge(
    left=sales_product_df,
    right=orders_customers_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)

# Mengelompokkan berdasarkan age_group dan product_type, lalu melakukan agregasi quantity_x dan total_price
grouped_age_product = all_df.groupby(by=["age_group", "product_type"]).agg({
    "quantity_x": "sum",  # Menjumlahkan kuantitas per kelompok
    "total_price": "sum"  # Menjumlahkan total harga per kelompok
}).reset_index()

# Menampilkan hasil agregasi berdasarkan age_group dan product_type
print("\nAgregasi berdasarkan age_group dan product_type:")
print(grouped_age_product)

# Menjumlahkan total item pesanan berdasarkan product_name
sum_order_items_df = all_df.groupby("product_name").quantity_x.sum().sort_values(ascending=False).reset_index()

# Menampilkan 15 produk teratas berdasarkan jumlah kuantitas
print("\n15 Produk teratas berdasarkan jumlah kuantitas:")
print(sum_order_items_df.head(15))

# Membuat canvas kosong
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
plt.show()  # Menampilkan canvas kosong
