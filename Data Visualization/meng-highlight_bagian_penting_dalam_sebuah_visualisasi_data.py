import matplotlib.pyplot as plt
import seaborn as sns

# Mengambil dataset penguins
penguins_df = sns.load_dataset("penguins")

# Membuat subset data untuk setiap spesies
adelie_df = penguins_df[penguins_df.species == "Adelie"]
chinstrap_df = penguins_df[penguins_df.species == "Chinstrap"]
gentoo_df = penguins_df[penguins_df.species == "Gentoo"]

# Membuat scatter plot untuk setiap spesies
plt.figure(figsize=(10, 5))
sns.scatterplot(data=adelie_df, x="body_mass_g", y="flipper_length_mm", color="lightgrey", label="Adelie")
sns.scatterplot(data=chinstrap_df, x="body_mass_g", y="flipper_length_mm", color="green", label="Chinstrap")
sns.scatterplot(data=gentoo_df, x="body_mass_g", y="flipper_length_mm", color="blue", label="Gentoo")

# Menambahkan legenda dan menampilkan plot
plt.legend()
plt.show()
