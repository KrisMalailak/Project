import pandas as pd

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
print("Statistik Deskriptif:\n", df.describe(include='all'))  # Menampilkan statistik deskriptif termasuk untuk kolom kategorikal

# Menampilkan matriks korelasi antar kolom numerik saja
numeric_df = df.select_dtypes(include=['number'])  # Memilih hanya kolom numerik
print("\nMatriks Korelasi:\n", numeric_df.corr())  # Menampilkan korelasi antar kolom numerik (Population dan Airports)






























