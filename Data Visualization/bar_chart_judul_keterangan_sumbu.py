import matplotlib.pyplot as plt
import pandas as pd

# Data kota dan populasi
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta', 'Surabaya', 'Medan', 'Makassar')

populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)

# Membuat DataFrame dari data kota dan populasi
df = pd.DataFrame({
    'Cities': cities,
    'Population': populations
})

# Mengurutkan DataFrame berdasarkan populasi
df.sort_values(by='Population', inplace=True)

# Membuat bar chart horizontal dengan data yang sudah diurutkan
plt.barh(y=df["Cities"], width=df["Population"])

# Menambahkan label dan judul untuk grafik
plt.xlabel("Population (Millions)")  # Mengganti label X
plt.ylabel('Cities')
plt.title("Population of Cities in Indonesia")  # Mengganti judul grafik

# Menampilkan grafik
plt.show()
