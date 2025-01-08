import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")


# Menampilkan 5 baris pertama dari dataframe
print(customers_df.head())  # Menampilkan 5 baris pertama


# Menampilkan informasi tentang dataframe
customers_df.info()    # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null


# Menghitung jumlah nilai NaN di dalam dataframe
print("\nJumlah nilai NaN di tiap kolom:")
print(customers_df.isna().sum())    # Menampilkan jumlah nilai NaN di setiap kolom


# Menghapus duplikasi
customers_df.drop_duplicates(inplace=True)  # Menghapus baris yang duplikat

# Mengisi nilai NaN pada kolom 'gender' dengan "Prefer not to say"
customers_df.fillna(value="Prefer not to say", inplace=True)


# Mengelompokkan data berdasarkan state dan menghitung unique customer_id
bystate_df =customers_df.groupby(by="state").customer_id.nunique().reset_index()


# Mengganti nama kolom customer_id menjadi customer_count
bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)


# Menampilkan dataframe berdasarkan state dan customer_count
print("\nJumlah pelanggan berdasarkan state:")
print(bystate_df)


# Visualisasi jumlah pelanggan berdasarkan state
plt.figure(figsize=(10, 5))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]  # Warna untuk visualisasi


sns.barplot(
    x="customer_count",
    y="state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
plt.title("Number of Customers by State", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show()