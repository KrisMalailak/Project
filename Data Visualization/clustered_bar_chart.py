import seaborn as sns
import matplotlib.pyplot as plt


# Memuat dataset penguins dari seaborn
penguins = sns.load_dataset("penguins")


# Membuat barplot dari dataset penguins
sns.barplot(data=penguins, x="species", y="body_mass_g", hue="sex", errorbar=None)


# Menampilkan plot
plt.show()