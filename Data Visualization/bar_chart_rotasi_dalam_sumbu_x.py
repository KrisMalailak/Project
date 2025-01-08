import matplotlib.pyplot as plt
 
# Data kota dan populasi
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')
 
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)
 
# Membuat bar chart dengan label kota di sumbu X dan populasi di sumbu Y
plt.bar(x=cities, height=populations)

# Memutar label sumbu X sebesar 45 derajat agar lebih mudah dibaca
plt.xticks(rotation=45)

# Menampilkan grafik
plt.show()
