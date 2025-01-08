import matplotlib.pyplot as plt


flavors =('Choclate', 'Vanilla', 'Macha', 'Others') # Tuple yang berisi nama-nama rasa es krim (Chocolate, Vanilla, Macha, Others)
votes = (50, 20, 30, 10)  # Tuple yang berisi jumlah suara untuk setiap rasa (50, 20, 30, 10)
colors = ('#8b4513', '#fff8dc', '#93c572', '#e67f0d' )  # Tuple yang berisi kode warna untuk setiap rasa. Misalnya, '#8b4513' adalah warna cokelat untuk Chocolate, '#fff8dc' adalah warna krem untuk Vanilla, dan seterusnya.
explode = (0.1, 0, 0, 0)    # Tuple yang menentukan elemen mana yang ingin "dimeledakkan" atau dibuat sedikit lebih terpisah dari lingkaran pie chart. Pada contoh ini, Chocolate (0.1) akan dipisahkan dari yang lain sedikit, sedangkan yang lain tetap pada posisi lingkaran biasa (0).


plt.pie(
    x=votes,            # Data yang digunakan untuk menentukan ukuran setiap bagian pie chart, yaitu jumlah suara untuk setiap rasa.
    labels=flavors,     # Menambahkan label pada setiap bagian pie chart berdasarkan nama-nama rasa es krim.
    autopct='%1.1f%%',  # Menambahkan persentase pada setiap bagian pie chart, ditampilkan dengan format desimal 1 digit, diikuti oleh tanda %.
    colors=colors,      # Mengatur warna untuk setiap bagian pie chart sesuai dengan warna yang ditentukan dalam colors.
    explode=explode     # Mengatur bagian Chocolate sedikit terpisah dari lingkaran pie chart (efek "meledak").
)


plt.show()  # Menampilkan pie chart yang sudah dibuat dengan semua pengaturan di atas.