import matplotlib.pyplot as plt


# Data rasa es krim dan jumlah vote
flavors = ('Chocolate', 'Vanilla', 'Macha', 'Others')
votes = (50, 20, 30, 10)
colors = ('#8b4513', '#fff8dc', '#93c572', '#E67f0d')
explode = (0.1, 0, 0, 0)


# Pie chart dengan properti wedgeprops untuk membuatnya seperti donut chart
plt.pie(
    x=votes,
    labels=flavors,
    colors=colors,
    wedgeprops={'width': 0.6}, # Menentukan lebar irisan (donut chart)
    autopct='%1.1f%%'   # Menampilkan persentase dengan satu desimal
)


# Menampilkan grafik
plt.show()