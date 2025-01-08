#===============#
# (Metode Numpy)#
#===============#
# import numpy as np

#jumlah_anjing = np.array([3,2,1,1,2,3,2,1,0,2])
#jumlah_anjing.mean()


# median merupakan parameter yang merepresentasikan nilai 
# tengah atau persentil ke-50 dari keseluruhan observasi atau data.
# import numpy as np

# jumlah_anjing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# np.median(jumlah_anjing)

#========================#
# (Metode scipt di Mode )#
#========================#
# import numpy  as np
# from scipy import stats

# jumlah_anjing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# mode_jumlah_anjing = stats.mode(jumlah_anjing)[0]

# print(mode_jumlah_anjing)
# hasilnya adalah 2 karena nilang yang sering muncul atau banyak

#========================#
# (Metode Numpy di range)#
#========================#
# import numpy as np

# jumlah_anjing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# range = jumlah_anjing.max() - jumlah_anjing.min()
# print(range)
# hasilnya adalah 3 karena nilai maximum mengurai nilai minumum (range = 3 - 0 = 3)


#======================================#
# (Metode Numpy di Interquartile Range)#
#======================================#
# import numpy as np

# jumlah_anjing =  np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# iqr = np.percentile(jumlah_anjing, 75) - np.percentile(jumlah_anjing, 25)
# print(iqr)
# hasilnya adalah 1.0 karena IQR dihitung untuk mengukur variabilitas data, 
# di mana nilai yang lebih besar menunjukkan bahwa data lebih tersebar, 
# sementara nilai yang lebih kecil menunjukkan bahwa data lebih terkonsentrasi


#============================#
# (Metode pandas di variance)#
#============================#
# import numpy as np
# import pandas as pd

# jumlah_anjing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# jumlah_anjing_series = pd.Series(jumlah_anjing)
# print(jumlah_anjing_series.var())
# hasilnya adalah 0.9000000000000001 karena Varians adalah ukuran statistik yang menunjukkan seberapa tersebar 
# data dari rata-rata. Dalam hal ini, varians sebesar 0.8 menunjukkan bahwa jumlah anjing yang diamati 
# dalam data tidak terlalu tersebar dari rata-rata, yang menunjukkan distribusi yang relatif seragam.

#===================================#
# (Metode Standard Deviation pandas)#
#===================================#
# import numpy as np
# import pandas as pd

# jumlah_anjing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# jumlah_anjing_series = pd.Series(jumlah_anjing)
# std_dev= jumlah_anjing_series.std()
# print(std_dev)
# hasilnya adalah 0.9486832980505139 simpangan baku dari data jumlah kucing adalah sekitar 0,948. 
# Ini berarti bahwa secara umum, jumlah kucing di setiap elemen dalam array tersebut berada sekitar 0,948 unit dari rata-rata jumlah kucing



#=================================================#
#(Metode Grafik histogram mengggunakan matplotlib)#
#=================================================#
# import numpy as np
# import matplotlib.pyplot as plt

# jumlah_anjing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# plt.hist(jumlah_anjing, bins=4)
# plt.show()
# # hasilnya adalah memperoleh grafik histogram left-skewed distribution yang kurang sempurna


# import numpy as np
# import matplotlib.pyplot as plt

# # Data warna yang diganti menjadi kode numerik
# data_warna = np.array(['merah', 'biru', 'hijau', 'merah', 'biru', 'biru', 'hijau', 'merah', 'biru', 'merah'])

# # Menghitung frekuensi setiap warna
# warna_unik, frekuensi = np.unique(data_warna, return_counts=True)

# # Membuat histogram
# plt.bar(warna_unik, frekuensi)
# plt.xlabel('Warna')
# plt.ylabel('Frekuensi')
# plt.title('Histogram Frekuensi Warna')
# plt.show()



#====================================#
#(Metode Skewness menggunakan pandas)#
#====================================#
# import numpy as np
# import pandas as pd

# jumlah_anjing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
# jumlah_anjing_series = pd.Series(jumlah_anjing)
# hasil_skew = jumlah_anjing_series.skew

# print(hasil_skew)
# hasilnya adalah nilai skewness sebesar -0.23. 
# Nilai tersebut menunjukkan bahwa data kita cenderung memiliki distribusi left-skewed.



#==============================================#
#(Metode Correlation dengan menggunakan pandas)#
#==============================================#
# import pandas as pd

# sample_data = {
#     'name' : ['Kris', 'Andre', 'Daniel', 'Lewi', 'Angga'],
#     'age' : [24, 22, 23, 25, 28],
#     'communication_skill_score' : [85, 70, 75, 90, 90],
#     'quantitative_skill_score' : [80, 90, 80, 75, 70],
# }

# df = pd.DataFrame(sample_data)


# # Menghitung korelasi antar kolom numerik
# correlation_matrix = df.corr(numeric_only=True)

# # Mencetak matriks korelasi
# print(correlation_matrix)
# Penjelasan nya = bahwa feature age dan communication_skill_score memiliki korelasi cukup bersesuaian. 
# Sebaliknya, feature age dan quantitative_skill_score memiliki korelasi yang sangat berlawanan.


#=============================================#
#(Metode Covariansi dengan menggunakan pandas)#
#=============================================#
# import pandas as pd

# sample_data = {
#     'name' : ['Natalie', 'Adin', 'Joko', 'Caca', 'Suparno'],
#     'age' : [24, 22, 23, 25, 28],
#     'communication_skill_score' : [85, 70, 75, 90, 90],
#     'quantitative_skill_score' : [80, 90, 80, 75, 70],
# }

# df = pd.DataFrame(sample_data)

# # Menghitung kovariansi anntar kolom numerik
# covariance_matrix = df.cov(numeric_only=True)

# # Mencetak matriks kovariansi
# print(covariance_matrix)
# Penjelasannya = nilai covariance yang diperoleh memiliki skala yang belum ternormalisasi.
# Inilah yang menjadi salah satu kesulitan dalam menginterpretasi nilai covariance dari sebuah data.



#=============================================#
#(Metode Pandas untuk membaca format csv)#
# ============================================#

# import pandas as pd

#  df = pd.read_csv("C:\Users\DELL\Documents\Project\Python", delimiter=",") File Path Salah: Pastikan file "data.csv" berada di direktori yang sama dengan skrip Python Anda atau berikan path lengkap ke file CSV.

# import csv

# with open("latihan_data.csv", "r") as filename:
#     csvdata = csv.reader(filename)
#     for row in csvdata:
#         print(row)


# import csv

# with open("latihan_data.csv", "r") as filename:
#     csvdata = csv.DictReader(filename)
#     for row in csvdata:
#         print(dict(row)) #csv.DictReader membaca file CSV dan menganggap baris pertama sebagai header. 
                         # Setiap baris selanjutnya akan dipetakan ke dalam dictionary dengan kunci sebagai nama kolom (header).


#==================================================#
#(Metode pandas untuk membaca format XLSX atau XLS)#
#==================================================#

# import pandas as pd
 
# df = pd.read_excel("latihan2_data.xlsx", sheet_name="Sheet1")

# print(df)


#==================================================#
#(Metode pandas untuk membaca Format berkas JSON)#
#==================================================#

# import pandas as pd #Mengimpor library Pandas, yang berguna untuk manipulasi dan analisis data.

# df = pd.read_json("latihan3_data.json") #Membaca file latihan3_data.json dan mengonversinya menjadi DataFrame Pandas (objek seperti tabel).

# print(df.head()) #Menampilkan lima baris pertama dari DataFrame, yang merupakan tampilan standar dari awal data.


# import pandas as pd 

# # Membaca file JSON
# df = pd.read_json('latihan3_data.json')

# # Mengubah format menjadi Excel  dan menyimpan
# df.to_excel('latihan3_data.xlsx', index=False)

# print("File berhasil dikonversi ke Excel")


#================================================#
#(Metode pandas untuk membaca Format berkas HTML)#
#================================================#

# import pandas as pd

# url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
# df = pd.read_html(url)[0]

# # Menampilkan isi DataFrame
# print(df.head())  # Menampilkan 5 baris pertama dari DataFrame


#===============================================#
#(Metode pandas untuk membaca Format berkas XML)#
#===============================================#

# import pandas as pd

# df = pd.read_xml("https://www.w3schools.com/xml/books.xml")

# print(df.head())


#==================================================#
#(Metode pandas untuk Akses data dari SQL database)#
#==================================================#


# import sqlite3

# # Membuat koneksi ke database
# conn = sqlite3.connect('mydatabase.db')

# # Membuat tabel
# conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# # Menambahkan data contoh
# conn.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
# conn.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
# conn.commit()
# conn.close()




# import pandas as pd
# import sqlalchemy as sqla
 
# db = sqla.create_engine("sqlite:///mydata.sqlite")
 
# # Membaca tabel dan menyimpan hasilnya ke dalam variabel df
# df = pd.read_sql_table("table_name", db)

# # Menampilkan hasilnya
# print(df)


#=================================================================================================================#
#(Metode pandas read_sql_query()untuk membaca SQL query dan mempresentasikannya ke dalam bentuk pandas DataFrame.)#
#=================================================================================================================#

# import pandas as pd
# import sqlalchemy as sqla

# # Membuat koneksi ke database
# db = sqla.create_engine("sqlite:///mydata.sqlite")

# # Membaca query SQL ke dalam DataFrame
# df = pd.read_sql_query("SELECT * FROM table_name", db)

# # Menampilkan DataFrame
# print(df)


#======================================================================================================================#
#(Metode pandas read_sql()untuk membaca SQL query atau table dan mempresentasikannya ke dalam bentuk pandas DataFrame.)#
#======================================================================================================================#


# import pandas as pd
# import sqlalchemy as sqla

# # Membuat koneksi ke database
# db = sqla.create_engine("sqlite:///mydata.sqlite")

# # Membaca query SQL ke dalam DataFrame
# df = pd.read_sql("SELECT * FROM table_name", db)

# # Menampilkan DataFrame
# print(df)


#======================================================#
#(Metode pandas untuk menggabungkan dua buah DataFrame)#
#======================================================#

# import pandas as pd

# # Membuat contoh DataFrame pertama
# product_df = pd.DataFrame({
#     'product_id' : [10, 20, 30, 40, 50],
#     'product_name' : ['Mobil', 'Pesawat', 'Sepeda', 'Kapal laut', 'Motor'],
#     'price' : [100, 200, 300, 400, 500]
# })

# # Membuat contoh DataFrame kedua
# order_df = pd.DataFrame({
#     'order_id' : [1, 2, 3, 4, 5],
#     'product_id' : [10, 20, 30, 40, 50],  # Mengganti dengan ID produk yang ada di product_df
#     'quantity' : [6, 7, 8, 9, 10]
# })

# # Menggabungkan dua DataFrame berdasarkan kolom product_id
# merged_df = pd.merge(
#     left=product_df,
#     right=order_df,  # Menggunakan order_df yang benar
#     how='inner',
#     left_on='product_id',
#     right_on='product_id'
# )

# # Menampilkan hasil gabungan
# print(merged_df)


# # Contoh Ke-2 #
# import pandas as pd

# # Membuat contoh DataFrame pertama
# product_df = pd.DataFrame({
#     'product_id': [101, 102, 103, 104],
#     'product_name': ['Laptop', 'Keyboard', 'Mouse', 'Monitor'],
#     'price': [1500, 100, 50, 300]
# })

# # Membuat contoh DataFrame kedua
# orders_df = pd.DataFrame({
#     'order_id': [1, 2, 3, 4],
#     'product_id': [101, 102, 104, 105],  # Ada satu product_id (105) yang tidak ada di product_df
#     'quantity': [2, 1, 4, 3]
# })

# # Menggabungkan dua DataFrame berdasarkan kolom product_id
# merged_df = pd.merge(
#     left=product_df,
#     right=orders_df,
#     how='inner',  # 'inner' akan menggabungkan hanya baris dengan product_id yang ada di kedua DataFrame
#     left_on='product_id',
#     right_on='product_id'
# )

# # Menampilkan hasil gabungan
# print(merged_df)


#====================================================================================================#
# (Metode Pandas untuk menangani missing values (nilai yang hilang) digunakan untuk membersihkan atau
# mempersiapkan dataset sebelum melakukan analisis lebih lanjut.)#
#====================================================================================================#


# import pandas as pd

# # Membaca file CSV dengan nama file yang benar dan lengkap
# try:
#     product_df = pd.read_csv("product.csv")
    
#     # Menampilkan jumlah nilai null di setiap kolom
#     null_counts = product_df.isnull().sum()
#     print(null_counts)

# except FileNotFoundError:
#     print("File 'product.csv' tidak ditemukan. Pastikan path dan nama file sudah benar.")
# except pd.errors.EmptyDataError:
#     print("File 'product.csv' kosong.")
# except pd.errors.ParserError:
#     print("Terjadi kesalahan saat memparsing file 'product.csv'.")


#========================================================================================================#
# (Metode pandas dengan Duplicate data untuk mengidentifikasi baris-baris duplikat dalam suatu DataFrame)#
#========================================================================================================#

# import pandas as pd


# # Membaca tabel dari URL
# url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
# df = pd.read_html(url)[0] # Membaca tabel pertama dari halaman

# # Menampilkan Dataframe untuk memastikan data telah diambil dengan benar
# print("DataFrame yang diambil:")
# print(df.head()) # Tempilkan beberapa baris pertama dari DataFrame

# # Menghitung jumlah baris duplikat
# duplicate_count = df.duplicated().sum()
# print(f"\njumlah baris duplikat: {duplicate_count}")

# # Menampilkan jumlah baris duplikat jika ada
# if duplicate_count > 0:
#     print("\nBaris duplikat:")
#     print(df[df.duplicated()])
# else:
#     print("\nTidak ada baris duplikat")


# import pandas as pd

# data = {'ID': [1, 2, 3, 4, 5, 1],
#         'Name': ['A', 'B', 'C', 'D', 'E', 'A']}

# df = pd.DataFrame(data)

# # Mengidentifikasi baris duplikat
# print(df.duplicated())

# # Menghapus duplikat
# df_clean = df.drop_duplicates()
# print(df_clean)


#======================================================================================#
# (Metode NumPy untuk menghitung outliers (nilai yang jauh di luar rentang normal data)
# menggunakan Interquartile Range (IQR))#
#======================================================================================#


# import numpy as np

# # Contoh data (pastikan data dalam bentuk list atau array)
# data = [10, 12, 14, 15, 16, 18, 21, 22, 25, 29, 34, 35, 37, 40]

# # Menghitung kuartil pertama (Q1) dan kuartil ketiga (Q3)
# q25, q75 = np.percentile(data, 25), np.percentile(data, 75)

# # Menghitung Interquartile Range (IQR)
# iqr = q75 - q25

# # Menentukan cut-off untuk mendeteksi outlier
# cut_off = iqr * 1.5

# # Menentukan nilai minimum dan maksimum untuk rentang normal data
# minimum, maximum = q25 - cut_off, q75 + cut_off

# # Mendeteksi outlier berdasarkan nilai minimum dan maksimum
# outliers = [x for x in data if x < minimum or x > maximum]

# # Menampilkan hasil outliers
# print("Outliers:", outliers)



# Contoh penggunaan IQR untuk mendeteksi outliers #

# import numpy as np
# data = [12, 15, 14, 10, 19, 28, 33, 47, 55, 14, 15, 30, 50, 60]


# # Menghitung kuartil 
# Q1 = np.percentile(data, 25)
# Q3 = np.percentile(data, 75)
# IQR =  Q3 - Q1


# # Menentukan cut-off untuk outliers
# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 - 1.5 * IQR


# # Menentukan outliers
# outliers = [x for x in data if x < lower_bound or x > upper_bound]
# print("Outliers:", outliers)


# Berikut adalah contoh bagaimana outliers mempengaruhi analisis regresi: #

# import  numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression


# # Contoh data dengan outliers
# X = np.array([1, 2, 3, 4, 5, 100]).reshape(-1, 1)
# y = np.array([1, 2, 3, 4, 5, 1000])

# # Menghilangkan outlier secara manual 
# # Mengambil hanya data yang tidak outliers (X < 10 dan y yang terkait)
# mask = X.flatten() < 10
# X_cleaned = X[mask] # Filter X tanpa outliers
# y_cleaned = y[mask] # filter y sesuai x yang tidak outliers


# # Linear regression tanpa outliers
# model = LinearRegression()
# model.fit(X_cleaned, y_cleaned)


# # Plotting garis regresi dari data tanpa outliears
# plt.plot(X_cleaned, model.predict(X_cleaned), color='Red', label='Regression line without outliers')


# # Menambahkan label dan judul
# plt.title("Linear Regression with Outliears Removed")
# plt.xlabel("X values")
# plt.ylabel("y values")
# plt.legend()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Contoh data dengan outliers
# X = np.array([1, 2, 3, 4, 5, 100]).reshape(-1, 1)
# y = np.array([1, 2, 3, 4, 5, 1000])

# # Menghilangkan outlier secara manual
# X_cleaned = X[X < 90].reshape(-1, 1)  # Hapus nilai X yang terlalu besar
# y_cleaned = y[:len(X_cleaned)]         # Hapus nilai y yang sesuai dengan X_cleaned

# # Linear regression tanpa outliers
# model = LinearRegression()
# model.fit(X_cleaned, y_cleaned)

# # Plotting data asli
# plt.scatter(X, y, color='blue', label='Data with outliers')
# plt.plot(X_cleaned, model.predict(X_cleaned), color='red', label='Regression line without outliers')

# # Menambahkan label dan judul
# plt.title("Linear Regression with Outliers Removed")
# plt.xlabel("X values")
# plt.ylabel("y values")
# plt.legend()
# plt.show()


#======================================================================================================#
# (Metode pandas untuk dropping adalah proses menghapus baris atau kolom tertentu dari suatu dataset.) #
#======================================================================================================#

# import pandas as pd


# # Membaca file CSV
# try:
#     products_df = pd.read_csv("product.csv")

#     # Menghapus baris yang mengandung nilai NaN
#     products_df.dropna(axis=0, inplace=True)

#     # Menampilkan hasil setelah penghapusan NaN
#     print(products_df)


# except FileNotFoundError:
#     print("File 'product.csv' tidak ditemukan. Pastikan path dan  nama file sudah benar.")
# except pd.errors.EmptyDataError:
#     print("File 'product.csv' kosong.")
# except pd.errors.ParserError:
#     print("Terjadi kesalahaan saat memparsing file 'product.csv'.")


#===================================================================================================#
# (Metode pandas untuk mengganti nilai yang hilang (missing values) dalam dataset dengan nilai lain,
# seperti nilai rata-rata, median, modus, atau nilai khusus lainnya.) #
#===================================================================================================#

# import pandas as pd

# # Membaca data dari file CSV
# data = pd.read_csv('employee_data.csv')

# # Mengisi nilai yang hilang di kolom 'age' dengan nilai rata-rata kolom 'age'
# data['age'].fillna(value=data['age'].mean(), inplace=True)

# # Menampilkan beberapa baris pertama untuk memastikan perubahan
# print(data.head())


#===================================================================================================#
# (Metode pandas menggunakan Interpolation untuk metode matematis yang digunakan untuk memperkirakan 
# nilai-nilai di antara titik-titik data yang sudah diketahui. ) #
#===================================================================================================#


# import pandas as pd

# # Membaca data dari file CSV
# data = pd.read_csv('latihan4_data.csv')


# # Memeriksa nama kolom 
# print("koom dalam data:", data.columns)


# # Menghapus spasi di nama kolom
# data.columns = data.columns.str.strip()


# # Memeriksa jumlah nilai hilang di kolom 'close_price'
# print("Jumlah nilai hilang di 'close_price':", data['close_price'].isnull().sum())


# # Mengisi nilai yang hilang di kolom 'close_price' dengan interpolasi linear
# data['close_price'].interpolate(method='linear', limit_direction='forward',inplace=True)


# # Menampilkan beberapa baris pertama untuk memastikan perubahan
# print(data.head())


#=======================================================================#
# (Metode pandas dengan Drop untuk mudah ialah men-drop atau menghapus
# seluruh baris yang mengandung outlier.) #
#=======================================================================#


# import pandas as pd

# # Membaca file CSV
# df = pd.read_csv("data.csv")

# # Menghapus baris dengan nilai kosong di kolom 'TotalCharges'
# df = df[df['TotalCharges'].notna()]

# # Mengonversi kolom 'TotalCharges' ke tipe numerik jika belum
# df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# # Menghapus kembali baris dengan nilai NaN yang mungkin muncul akibat konversi
# df = df[df['TotalCharges'].notna()]

# # Menghitung Q1, Q3, dan IQR untuk kolom 'TotalCharges'
# Q1 = df['TotalCharges'].quantile(0.25)
# Q3 = df['TotalCharges'].quantile(0.75)
# IQR = Q3 - Q1

# # Menentukan batas maksimum dan minimum untuk mendeteksi outlier
# maximum = Q3 + (1.5 * IQR)
# minimum = Q1 - (1.5 * IQR)

# # Kondisi untuk outliers (nilai di bawah minimum atau di atas maksimum)
# kondisi_lower_than = df['TotalCharges'] < minimum
# kondisi_more_than = df['TotalCharges'] > maximum

# # Menghapus baris yang merupakan outliers
# df.drop(df[kondisi_lower_than].index, inplace=True)
# df.drop(df[kondisi_more_than].index, inplace=True)

# # Menampilkan hasil akhir setelah outliers dihapus
# print(df.head())

# Menghitung nilai mahasiswa #

# import pandas as pd

# # Membaca file CSV yang berisi data mahasiswa
# df = pd.read_csv("data_mahasiswa.csv", sep=',')  # Ganti ',' dengan ';' jika perlu

# # Menampilkan nama kolom untuk verifikasi
# print("Nama kolom:", df.columns)

# # Memastikan kolom 'TotalCharges' ada dalam DataFrame
# if 'TotalCharges' not in df.columns:
#     print("Kolom 'TotalCharges' tidak ditemukan dalam data.")
# else:
#     # Menghapus baris dengan nilai kosong di kolom 'TotalCharges'
#     df = df[df['TotalCharges'].notna()]

#     # Mengonversi kolom 'TotalCharges' ke tipe numerik
#     df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#     # Menghapus kembali baris dengan nilai NaN yang mungkin muncul akibat konversi
#     df = df[df['TotalCharges'].notna()]

#     # Menghitung jumlah mahasiswa dengan nilai TotalCharges di atas 75
#     df_passed = df[df['TotalCharges'] > 75]

#     # Menampilkan mahasiswa yang memiliki nilai TotalCharges > 75
#     print("Mahasiswa yang memiliki nilai di atas 75:")
#     print(df_passed[['Nama', 'TotalCharges']])  # Asumsi kolom 'Nama' ada di dalam dataset

#     # Menghitung jumlah mahasiswa yang lolos
#     jumlah_mahasiswa_lolos = df_passed.shape[0]
#     print(f"Jumlah mahasiswa dengan nilai TotalCharges di atas 75: {jumlah_mahasiswa_lolos}")

#     # (Opsional) Menyimpan hasil ke file CSV
#     df_passed.to_csv("mahasiswa_lolos_totalcharges.csv", index=False)
#     print("Data mahasiswa yang lolos disimpan ke 'mahasiswa_lolos_totalcharges.csv'")


#==================================================================================================#
# (Metode pandas dengan Imputation untuk mengisi nilai yang hilang (missing values) dalam dataset) #
#==================================================================================================#


# import pandas as pd


# # Membaca file CSV yang berisi data
# df = pd.read_csv("latihan5_data.csv")


# # Menghitung Q1, Q3, dan IQR
# Q1 = df['TotalCharges'].quantile(0.25)
# Q3 = df['TotalCharges'].quantile(0.75)
# IQR = Q3 - Q1


# # Menentukan batas maksimum dan minimum untuk outliers
# maximum = Q3 + (1.5 * IQR)
# minimum = Q1 - (1.5 * IQR)


# # Menentukan kondisi untuk outliers
# kondisi_lower_that = df['TotalCharges'] < minimum
# kondisi_more_that = df['TotalCharges'] > maximum


# # Mengganti nilai outliers dengan batas maksumim dan minimum
# df.loc[kondisi_more_that, 'TotalCharges'] = maximum
# df.loc[kondisi_lower_that, 'TotalCharges'] = minimum


# # Menampilkan hasil setelah outliers diubah
# print(df)
 

#===========================================================#
# (Metode pandas dengan Duplicate Data) #
#===========================================================#

# import pandas as pd


# # Membaca file CSV yang berisi data
# try:
#     df = pd.read_csv("latihan6_data.csv")
#     print("File CSV berhasil dibaca.")
# except FileNotFoundError:
#     print("File tidak di temukan, pastikan file 'latihan6_data.csv' ada di rektori yang benar.")
#     exit()


# # Menampilkan data sebelumnya penghapus duplikat
# print("Data sebelumnya penghapus duplikat:")
# print(df)


# # Menghapus baris duplikat berdasarkan semua kolom
# df.drop_duplicates(inplace=True)


# # Menampilkan data setelah penghapusan duplikat
# print("Data setelah penghapusan duplikasi:")
# print(df)


# # (opsional) Menyimpan data tanpa duplikasi ke file CSV baru
# df.to_csv("data_no_duplicates.csv", index=False)
# print("Data tanpa duplikat disimpan ke 'data_no_duplocates.csv'")


# (Duplicates Data dalam umur mahasiswa kelas A dan B di mata kuliah Struktur Data)

# import pandas as pd

# # Membaca file CSV yang berisi data
# try:
#     df = pd.read_csv("latihan6_v2_data.csv")
#     print("File CSV berhasil dibaca.")
# except FileNotFoundError:
#     print("File tidak diterimukan, pastikan file 'latihan6_v2_data.csv' ada di direktori yang benar.")
#     exit()


# # Menampilkan data sebelum penghapusan duplikat 
# print("Data sebelum penghapus duplikasi:")
# print(df)

# # Menghapus baris duplikat berdasarkan 'Kelas', 'Mata Kuliah' (Struktur Data), dan 'Umur'
# # asumsi kolom 'Kelas', 'Mata Kuliah', dan 'Umur' ada di dalam dataset
# df.drop_duplicates(subset=['Kelas', 'Mata Kuliah', 'Umur'],inplace=True)


# # Menampilkan data setelah menghapus duplikat
# print("Data sebelum penghapusan duplikat:")
# print(df)


# # (Opsional) Menyimpan data tanpa duplikat ke file CSV baru
# df.to_csv("datav2_no_duplicates.csv", index=False)
# print("Data tanpa duplikat disimpan ke 'datav2_no_duplicates.csv'")














