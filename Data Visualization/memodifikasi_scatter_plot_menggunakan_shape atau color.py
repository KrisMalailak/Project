import seaborn as sns
import matplotlib.pyplot as plt


# Memuat dataset penguins dari seaborn
penguins = sns.load_dataset("penguins")


# Membuat scatterplot dengan seaborn
sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="species", style="species")


# Menampilkan grafik
plt.show()