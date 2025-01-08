import pandas as pd


# Membaca file CSV dari URL
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")


# Menampilkan 5 baris pertama dari dataframe customers
print(customers_df.head())  # Menampilkan 5 baris pertama


# Menampilkan informasi tentang dataframe
customers_df.info()    # Menampilkan informasi kolom, tipe data, dan jumlah nilai non-null


# Menghitung jumlah nilai NaN di dalam dataframe
print("\nJumlah nilai NaN di tiap kolom:")
print(customers_df.isna().sum())  # Menampilkan jumlah nilai NaN di setiap kolom


# Menghitung jumlah duplikasi sebelum penghapusan
print("\nJumlah duplikasi sebelum penghapusan: ", customers_df.duplicated().sum())   # Menghitung jumlah duplikasi baris


# Menghapus duplikasi
customers_df.drop_duplicates(inplace=True)  # Menghapus baris duplikat


# Menghapus jumlah duplikasi setelah penghapusan
print("\nJumlah duplikasi setelah penghapusan: ", customers_df.duplicated().sum())  # Mengecek apakah duplikasi sudah dihapus


# Menampilkan statistik deskriptif dari dataframe
print("\nStatistik deskriptif dari dataframe(kolom numerik):")
print(customers_df.describe())   # Menampilkan statistik deskriptif dari kolom numerik


# Mengisi nilai NaN pada kolom gender dengan "Prefer not to say"
customers_df.fillna(value="Prefer not to say", inplace=True)  # Mengganti nilai NaN kolom 'gender'


# Menghitung dan menampilkan frekuensi nilai pada kolom 'gender'
print("\nFrekuensi nilai pada kolom 'gender':")
print(customers_df.gender.value_counts())   # Menghitung dan menampilkan frekuensi nilai di kolom 'gender'


# Memeriksa kembali apakah masih ada nilai NaN setelah pengisian
print("\nJumlah nilai NaN setelah pengisian:")
print(customers_df.isna().sum())  # Mengecek apakah masih ada nilai NaN


# Menampilkan baris pelanggan yang meniliki umur tinggi sebelum pergantian
print("\nBaris pelanggan dengan umur tertinggi sebelum penggantian:")
print(customers_df[customers_df.age == customers_df.age.max()])   # Menampilkan baris dengan umur maksimal


# Mengganti nilai umur maksimal dengan 70
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)   # Mengganti nilai umur maksimal dengan 70


# Menampilkan baris pelanggan dengan umur tertinggi setelah penggantian
print("\nBaris pelanggan dengan umur tertinggi setelah pergantian:")
print(customers_df[customers_df.age == customers_df.age.max()])   # Menampilkan baris dengan umur maksimal setelah perubahan


# Menampilkan kembali statistik deskriptif untuk melihat perubahan
print("\nStatistik deksriptif setelah mengganti umur maksimum menjadi 70:")
print(customers_df.describe())   # Menampilkan statistik deskriptif setelah perubahan


# Mengganti nilai umur maksimum dengan 50
customers_df.age.replace(customers_df.age.max(), 50, inplace=True)   # Mengganti nilai umur maksimal dengan 50  


# Menampilkan statistik deksriptif setelah mengganti umur maksimum menjadi 50
print("\nStatistik deksriptif setelah mengganti umur maksimum menjadi 50:")
print(customers_df.describe())   # Menampilkan statistik deskriptif setelah perubahan


# Menampilkan statistik deksriptif dari semua kolom (termasuk kategorikal)
print("\nStatistik deskriptif dari semua kolom (numerik dan kategorikal):")
print(customers_df.describe(include="all"))  


# Mengelompokkan data berdasarkan gender dan melakukan agregasi
print("\nAgregasi berdasarkan gender:")
gender_agg = customers_df.groupby(by="gender").agg({
    "customer_id": "nunique",   # Menghitung jumlah unique customer_id per gender
    "age": ["max", "min", "mean", "std"]    # Menghitung statistik umur (max, min, mean, std) per gender
})
print(gender_agg)


# Mengelompokan data berdasarkan city dan menghitung unique customers_id, lalu mengurutkan secara descending
print("\nJumlah unique customers_id per city:")
city_agg = customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False)
print(city_agg)


# Mengelompokkan data berdasarkan state dan menghitung unique customers_id, lalu mengurutkan secara descending
print("\nJumlah uniquq customers_id per state:")
state_agg = customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=False)
print(state_agg)


# Menambah kolom 'status' berdasarkan customer_id di order_df
customer_id_in_orders_df = orders_df.customer_id.tolist()
customers_df["status"] = customers_df["customer_id"].apply(lambda x: "Active" if x in customer_id_in_orders_df else "Non active")


# Menampilkan 5 baris secara acak dengan kolom status baru
print("\n5 Sampel dari dataframe customers dengan kolom 'status':")
print(customers_df.sample(5))


# Menghitung jumlah customer_id berdasarkan status
print("\nJumlah customer_id berdasarkan status:")
print(customers_df.groupby(by="status").customer_id.count())


# Melakukan merge antara order_df customers_df berdasarkan customer_id
orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)


# Menampilkan 5 baris pertama dari dataframe yang digabung
print("\n5 Baris pertama dari dataframe hasil penggabungan:")
print(orders_customers_df.head())


# Mengelompokkan data berdasarkan city dan menghitung unique order_id, lalu mengurutkan secara descending
print("\nJumlah unique order_id per city:")
city_orders_agg = orders_customers_df.groupby(by="city").order_id.nunique().sort_values(ascending=False).reset_index().head(10)
print(city_orders_agg)


# Mengelompokkan data berdasarkan state dan menghiung unique order_id, lalu mengeurutkan descending
print("\nJumlah unique order_id per state:")
state_orders_agg = orders_customers_df.groupby(by="state").order_id.nunique().sort_values(ascending=False).reset_index()
print(state_orders_agg)


# Mengelompokkan data berdasarkan gender dan menghitung unique order_id, lalu mengurutkan secera descending
print("\nJumlah unique order_id per gender:")
gender_orders_agg = orders_customers_df.groupby(by="gender").order_id.nunique().sort_values(ascending=False).reset_index()
print(gender_orders_agg)


# Menambahkan kolom 'age_group' berdasarkan umur
orders_customers_df["age_group"] = orders_customers_df.age.apply(lambda x: "Youth" if x <= 24 else ("Seniors" if x > 64 else "Adults"))


# Mengelompokkan data berdasarkan age_group dan menghitung unique order_id
print("\nJumlah unique order_id per age_group:")
age_group_orders_agg = orders_customers_df.groupby(by="age_group").order_id.nunique().sort_values(ascending=False).reset_index()
print(age_group_orders_agg)