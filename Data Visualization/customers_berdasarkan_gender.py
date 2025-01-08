# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt


# # Membaca file CSV dari URL
# customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")


# # Menghapus duplikasi
# customers_df.drop_duplicates(inplace=True)    # Mengahapus baris yang duplikat


# # Mengisi nilai NaN pada kolom gender dengan "Prefer not to say"
# customers_df.fillna(value="Prefer not to say", inplace=True)  # Mengganti nilai NaN di kolom 'gender'


# # Mengelompokkan data berdasarkan gender dan menghitung unique customers_id
# bygender_df = customers_df.groupby(by="gender").customer_id.nunique().reset_index()


# # Mengganti nama kolom untuk lebih mudah dipahami
# bygender_df.rename(columns={
#     "customer_id" : "customer_count"
# }, inplace=True)


# # Membuat palet warna untuk visualisasi
# color = sns.color_palette("Set2")


# # Membuat plot bar untuk jumlah pelanggan berdasarkan gender 
# plt.figure(figsize=(10, 5))


# sns.barplot(
#     y="customer_count",
#     x="gender",
#     data=bygender_df.sort_values(by="customer_count", ascending=False),
#     palette=color
# )


# # Menambahkan judul dan mengatur tampilan
# plt.title("Number of Customers by Gender", loc="center", fontsize=15)
# plt.ylabel(None)
# plt.xlabel(None)
# plt.tick_params(axis='x', labelsize=12)


# # Menampilkan plot
# plt.show()



























import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")

# Menghapus duplikasi
customers_df.drop_duplicates(inplace=True)  # Menghapus baris yang duplikat

# Mengisi nilai NaN pada kolom gender dengan "Prefer not to say"
customers_df.fillna(value="Prefer not to say", inplace=True)  # Mengganti nilai NaN di kolom 'gender'

# Analisis berdasarkan gender
# Mengelompokkan data berdasarkan gender dan menghitung unique customer_id
bygender_df = customers_df.groupby(by="gender").customer_id.nunique().reset_index()

# Mengganti nama kolom untuk lebih mudah dipahami
bygender_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

# Membuat palet warna untuk visualisasi
colors = sns.color_palette("Set2")

# Membuat plot bar untuk jumlah pelanggan berdasarkan gender
plt.figure(figsize=(10, 5))

sns.barplot(
    y="customer_count", 
    x="gender",
    data=bygender_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)

# Menambahkan judul dan mengatur tampilan
plt.title("Number of Customers by Gender", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)

# Menampilkan plot
plt.show()


# Analisis berdasarkan kelompok usia
# Mengelompokkan usia ke dalam grup (Youth, Adults, Seniors)
bins = [0, 24, 64, 100]
labels = ["Youth", "Adults", "Seniors"]
customers_df['age_group'] = pd.cut(customers_df['age'], bins=bins, labels=labels)

# Mengelompokkan data berdasarkan age_group dan menghitung unique customer_id
byage_df = customers_df.groupby(by="age_group").customer_id.nunique().reset_index()

# Mengganti nama kolom untuk lebih mudah dipahami
byage_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

# Mengurutkan berdasarkan kategori usia
byage_df['age_group'] = pd.Categorical(byage_df['age_group'], ["Youth", "Adults", "Seniors"])

# Membuat plot bar untuk jumlah pelanggan berdasarkan kelompok usia
plt.figure(figsize=(10, 5))
colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3"]

sns.barplot(
    y="customer_count", 
    x="age_group",
    data=byage_df.sort_values(by="age_group", ascending=False),
    palette=colors_
)

# Menambahkan judul dan mengatur tampilan
plt.title("Number of Customers by Age Group", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)

# Menampilkan plot
plt.show()
