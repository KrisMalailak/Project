import matplotlib.pyplot as plt
 
# Data kota dan populasi
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')
 
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)
 
# Membuat bar chart horizontal dengan label kota di sumbu Y dan populasi di sumbu X
plt.barh(y=cities, width=populations)

# Menampilkan grafik
plt.show()
