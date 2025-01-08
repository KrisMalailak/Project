import pandas as pd
import matplotlib.pyplot as plt
 
# Data yang diberikan
city_names = ['Jakarta', 'Bandung', 'Makassar', 'Surabaya', 'Medan', 'Yogyakarta', 'Malang']
population = [498044, 964254, 491918, 8398748, 653115, 883305, 744955]
num_airports = [2, 2, 8, 3, 1, 3, 2]

# Membuat DataFrame
df = pd.DataFrame({
  'City Name': city_names,
  'Population': population, 
  'Airports': num_airports,
})

# Menampilkan statistik deskriptif
print(df.describe(include='all'))  # Menampilkan statistik deskriptif termasuk untuk kolom kategorikal


# Menampilkan histogram 
df.hist(bins=10, figsize=(10,5))  # Menampilakn histrogram dari kolom numerik
plt.show()  # Menampilkan plot