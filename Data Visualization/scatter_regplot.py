import matplotlib.pyplot as plt
import seaborn as sns


# Data diameter dan berat lemon
lemon_diameter = [6.44, 6.87, 7.7, 8.85, 8.15, 9.96, 7.21, 10.04, 10.2, 11.06]
lemon_weight = [112.05, 114.58, 116.71, 117.4, 128.93, 132.93, 138.92, 145.98, 148.44, 152.81]


# Membuat regresi plot menggunakan seaborn
sns.regplot(x=lemon_diameter, y=lemon_weight)


#  Menampilkan grafik
plt.show()