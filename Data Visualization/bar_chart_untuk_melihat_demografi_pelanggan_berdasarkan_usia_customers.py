import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")

# Menampilkan 5 baris pertama dari dataframe
print(customers_df.head())  # Menampilkan 5 baris pertama

# Menampilkan informasi tentang dataframe
customers_df.info()   # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null

# Menghitung jumlah nilai NaN di dalam dataframe
print("\nJumlah nilai NaN di tiap kolom:")
print(customers_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom 

# Menghitung jumlah duplikasi sebelum penghapusan
print("\nJumlah duplikasi sebelum penghapusan: ", customers_df.duplicated().sum())   # Menghitung jumlah duplikasi baris

# Menghapus duplikasi
customers_df.drop_duplicates(inplace=True)  # Menghapus baris yang duplikat

# Menghitung jumlah duplikasi setelah penghapusan
print("\nJumlah duplikasi setelah penghapusan: ", customers_df.duplicated().sum())   # Mengecek apakah duplikasi sudah dihapus

# Menampilkan statistik deskriptif dari dataframe
print("\nStatistik deskriptif dari dataframe (kolom numerik):")
print(customers_df.describe())    # Menampilkan statistik deskriptif dari kolom numerik

# Mengisi nilai NaN pada kolom gender dengan "Prefer not to say"
customers_df.fillna(value="Prefer not to say", inplace=True)  # Mengganti nilai NaN di kolom 'gender'

# Menghitung dan menampilkan frekuensi nilai pada kolom 'gender'
print("\nFrekuensi nilai pada kolom 'gender':")
print(customers_df.gender.value_counts())     # Menghitung dan menampilkan frekuensi nilai di kolom 'gender'

# Memeriksa kembali apakah masih ada nilai NaN setelah pengisian
print("\nJumlah nilai NaN setelah pengisian:")
print(customers_df.isna().sum())   # Mengecek apakah masih ada nilai NaN

# Menampilkan baris pelanggan yang memiliki umur tertinggi sebelum penggantian
print("\nBaris pelanggan dengan umur tertinggi sebelum penggantian:")
print(customers_df[customers_df.age == customers_df.age.max()])   # Menampilkan baris dengan umur maksimal

# Mengganti nilai umur maksimum dengan 70
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)  # Mengganti nilai umur maksimal dengan 70

# Menampilkan baris pelanggan dengan umur tertinggi setelah penggantian
print("\nBaris pelanggan dengan umur tertinggi setelah penggantian:")
print(customers_df[customers_df.age == customers_df.age.max()])   # Menampilkan baris dengan umur maksimal setelah perubahan

# Menampilkan kembali statistik deskriptif untuk melihat perubahan
print("\nStatistik deskriptif setelah mengganti umur maksimum menjadi 70:")
print(customers_df.describe())    # Menampilkan statistik deskriptif setelah perubahan

# Mengganti nilai umur maksimum dengan 50
customers_df.age.replace(customers_df.age.max(), 50, inplace=True)  # Mengganti nilai umur maksimal dengan 50

# Menampilkan statistik deskriptif setelah mengganti umur maksimum menjadi 50
print("\nStatistik deskriptif setelah mengganti umur maksimum menjadi 50:")
print(customers_df.describe())    # Menampilkan statistik deskriptif setelah perubahan

# Menampilkan statistik deskriptif dari semua kolom (termasuk kategorikal)
print("\nStatistik deskriptif dari semua kolom (numerik dan kategorikal):")
print(customers_df.describe(include="all"))

# Mengelompokkan data berdasarkan gender dan melakukan agregasi
print("\nAgregasi berdasarkan gender:")
gender_agg = customers_df.groupby(by="gender").agg({
    "customer_id": "nunique",  # Menghitung jumlah unique customer_id per gender
    "age": ["max", "min", "mean", "std"]  # Menghitung statistik umur (max, min, mean, std) per gender
})
print(gender_agg)

# Mengelompokkan data berdasarkan city dan menghitung unique customers_id, lalu mengurutkan secara descending
print("\nJumlah unique customers_id per city:")
city_agg = customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False)
print(city_agg)

# Mengelompokkan data berdasarkan state dan menghitung unique customers_id lalu mengurutkan secera descending
print("\nJumlah unique customers_id per state:")
state_agg = customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=False)
print(state_agg)

# Menambahkan kolom 'age_group' untuk demografi berdasarkan usia
bins = [0, 25, 55, 100]
labels = ["Youth", "Adults", "Seniors"]
customers_df["age_group"] = pd.cut(customers_df["age"], bins=bins, labels=labels)

# Mengelompokkan data berdasarkan age_group dan menghitung unique customers_id
byage_df = customers_df.groupby(by="age_group").customer_id.nunique().reset_index()
byage_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

# Mengubah urutan kategori 'age_group'
byage_df['age_group'] = pd.Categorical(byage_df['age_group'], ["Youth", "Adults", "Seniors"])

# Visualisasi barplot demografi pelanggan berdasarkan usia
plt.figure(figsize=(10, 5))
colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3"]

sns.barplot(
    y="customer_count", 
    x="age_group",
    data=byage_df.sort_values(by="age_group", ascending=False),
    palette=colors_
)
plt.title("Number of Customer by Age Group", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()