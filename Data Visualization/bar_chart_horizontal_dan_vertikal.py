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

# Membuat figure dengan dua subplots: satu untuk bar chart vertikal dan satu untuk horizontal
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Grafik batang vertikal
axs[0].bar(x=df["Cities"], height=df["Population"])
axs[0].set_xlabel('Cities')
axs[0].set_ylabel('Population (Millions)')
axs[0].set_title('Vertical Bar Chart: Population of Cities in Indonesia')
axs[0].tick_params(axis='x', rotation=45)  # Memutar label kota

# Grafik batang horizontal
axs[1].barh(y=df["Cities"], width=df["Population"])
axs[1].set_xlabel('Population (Millions)')
axs[1].set_ylabel('Cities')
axs[1].set_title('Horizontal Bar Chart: Population of Cities in Indonesia')

# Menata layout agar grafik tidak saling tumpang tindih
plt.tight_layout()

# Menampilkan grafik
plt.show()
