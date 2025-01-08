import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt  # Pastikan untuk mengimpor matplotlib

# Menghasilkan data acak dari distribusi normal
x = np.random.normal(15, 5, 250)

# Membuat histogram menggunakan seaborn
sns.histplot(x=x, bins=15, kde=True)  # Menambahkan KDE (Kernel Density Estimate) jika diinginkan

# Menambahkan judul dan label
plt.title('Histogram with Seaborn')  # Menambahkan judul
plt.xlabel('Value')  # Menambahkan label sumbu X
plt.ylabel('Frequency')  # Menambahkan label sumbu Y

# Menampilkan grafik
plt.show()  # Gunakan plt.show() untuk menampilkan grafik
