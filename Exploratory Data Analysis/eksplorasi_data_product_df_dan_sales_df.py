import pandas as pd

# Membaca file CSV dari URL
product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")

# Menampilkan 5 baris pertama dari dataframe
print(product_df.head())  # Menggunakan print untuk menampilkan output

# Menampilkan informasi tentang dataframe
product_df.info()  # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null

# Menghitung jumlah duplikasi
print("Jumlah duplikasi: ", product_df.duplicated().sum())

# Menampilkan deskripsi dari dataframe
print("\nStatistik deskriptif dari dataframe (kolom numerik):")
print(product_df.describe())   # Menampilkan statistik deskriptif dari dataframe

# Menampilkan deskripsi dari dataframe, termasuk kolom kategorikal
print("\nStatistik deskriptif dari dataframe (termasuk kategorikal):")
print(product_df.describe(include="all"))


# Mengurutkan dataframe berdasarkan harga dalam urutan menurun
sorted_product_df = product_df.sort_values(by="price", ascending=False)


# Menampilkan 5 baris pertama dari dataframe yang sudah diurutkan
print("\n5 Baris teratas dari dataframe yang diurutkan berdasarkan harga (tertinggi):")
print(sorted_product_df.head())   # Menampilkan 5 baris pertama dari dataframe yang sudah diurutkan


# Mengelompokkan data berdasarkan product_type dan melakukan agregasi
print("\nAgregasi berdasarkan product_type:")
product_type_agg = product_df.groupby(by="product_type").agg({
    "product_id": "nunique",     # Menghitung jumlah unique product_id per product_type
    "quantity": "sum",           # Menjumlahkan quantity per product_type
    "price": ["min", "max"]      # Menampilkan harga minimum dan maksimum per product_type
})
print(product_type_agg)


# Mengelompokkan data berdasarkan product_name dan melakukan agregasi
print("\nAgregasi berdasarkan product_name:")
product_name_agg = product_df.groupby(by="product_name").agg({
    "product_id": "nunique",   # Menghitung jumlah unique product_id per product_name
    "quantity": "sum",         # Menjumlahkan quantity per product_name
    "price": ["min","max"]     # Menampilkan harga minimum dan maksimum per product_name

})
print(product_name_agg)


# Mengamsumsikan ada DataFrame sales_df yang juga akan dianalisis
# Membaca file CSV dari URL untuk sales_df
sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")


# Menampilkan deskripsi dari sales_df, termasuk kolom kategorikal
print("\nStatistik deskriptif dari sales_df(termasuk kategorikal):")
print(sales_df.describe(include="all"))


# Melakukan merge antara sales_df dan product_df berdasarkan product_id
sales_product_df = pd.merge(
    left=sales_df,
    right=product_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)


# Menampilkan 5 baris pertama dari dataframe hasil penggabungan
print("\n5 Baris pertama dari dataframe hasil penggabungan sales_df dan product_id:")
print(sales_product_df.head())


# Mengelompokkan data berdasarkan product_type dan melakukan agregasi setelah penggabungan
print("\nAgregasi berdasarkan product_type setelah penggabungan:")
sales_product_agg = sales_product_df.groupby(by="product_type").agg({
    "sales_id": "nunique",      # Menghitung jumlah unique sales_id per product_type
    "quantity_x": "sum",        # Menjumlahkan quantity_x (jumlah perjualan) per product_type
    "total_price": "sum",       # Menjumlahkan total_price per product_type
})
print(sales_product_agg)


# Mengelompokkan data berdasarkan product_name, melakukan agregasi, dan mengurutkan berdasarkan total_price
print("\nAgregasi berdasrkan product_name setelah penggabungan dan diurutkan berdasarkan total_price:")
sales_product_name_agg = sales_product_df.groupby(by="product_name").agg({
    "sales_id": "nunique",     # Menghitung jumlah unique sales_id per product_name
    "quantity_x": "sum",       # Menjumlahkan quantity_x (jumlah penjualan) per product_name
    "total_price": "sum"       # Mengjumlahkan total_price per product_name
}).sort_values(by="total_price", ascending=False)


print(sales_product_name_agg)