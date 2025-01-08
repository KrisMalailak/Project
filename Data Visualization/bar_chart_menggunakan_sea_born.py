import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# data kota dan populasi
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta',
          'Surakarta', 'Surabaya', 'Medan', 'Makassar')


populations = (45077604, 11626410, 212162757, 19109629, 50819826, 17579085, 3481, 287750, 785409)


# Membuat DataFrame dari data kota dan populasi
df = pd.DataFrame({
    'Cities' : cities,
    'Population' : populations
})


# Mengurutkan DataFrame berdasarkan populasi
df.sort_values(by='Population', inplace=True)


# Membuat bar chart horizontal menggunakan seaborn
sns.barplot(y=df["Cities"], x=df["Population"], orient="h", color='blue')


# Menambahkan label dan judul untuk grafik
plt.xlabel("Population (millions)")
plt.title("Popolation of Cities in Indonesia")


# Menampilakn grafik
plt.show()