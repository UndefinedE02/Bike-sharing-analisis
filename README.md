Bike Sharing Analysis Project
=============================

**Deskripsi Proyek**

Proyek ini bertujuan untuk menganalisis pola penggunaan sepeda berdasarkan berbagai faktor, seperti cuaca, musim, dan hari dalam seminggu. Selain itu, dilakukan analisis clustering untuk memahami pola peminjaman sepeda lebih lanjut.

**Struktur Folder**

submission
- dashboard
   - main_data.csv
   - dashboard.py
- data
   - data_1.csv
   - data_2.csv
   - merged_data.csv
- notebook.ipynb
- README.md
- requirements.txt
- url.txt

**Tujuan Analisis**

Menganalisis pola penggunaan sepeda berdasarkan waktu (jam, hari, musim).
Mengidentifikasi hubungan antara kondisi cuaca (suhu, kelembaban, kecepatan angin) dan jumlah penyewaan sepeda.
Melakukan clustering untuk memahami pola peminjaman sepeda.
Metode dan Implementasi
Eksplorasi Data: Menggunakan Pandas untuk melihat struktur data dan menganalisis statistik deskriptif.
Pembersihan Data: Menghapus duplikasi dan menangani nilai yang hilang.
Visualisasi Data: Menggunakan Matplotlib dan Seaborn untuk membuat grafik tren dan korelasi.
Clustering: Menggunakan metode K-Means untuk mengelompokkan pola peminjaman sepeda.
Dashboard Interaktif: Dibangun dengan Streamlit (dashboard.py).

**Cara Menjalankan Proyek**

1️.Instalasi Dependensi
Pastikan Anda sudah menginstal semua pustaka yang dibutuhkan dengan menjalankan perintah berikut:
pip install -r requirements.txt

2️.Menjalankan Notebook Jupyter
Buka Jupyter Notebook dan jalankan notebook.ipynb untuk melakukan eksplorasi dan analisis data.

3️.Menjalankan Dashboard Streamlit
Jalankan perintah berikut untuk membuka dashboard interaktif:
streamlit run dashboard/dashboard.py

**Hasil Analisis**

Hubungan Cuaca dan Penyewaan Sepeda:
Suhu memiliki korelasi positif dengan jumlah penyewaan sepeda.
Kelembaban tinggi cenderung menurunkan jumlah penyewaan sepeda.
Kecepatan angin tidak terlalu berpengaruh signifikan.
Pola Penggunaan Sepeda Berdasarkan Waktu:
Hari kerja memiliki pola penggunaan yang berbeda dibandingkan akhir pekan.
Penggunaan sepeda cenderung meningkat pada musim panas dan menurun pada musim dingin.

Clustering Pola Penggunaan:
Pengguna dapat dikelompokkan ke dalam beberapa kategori berdasarkan pola penyewaan mereka.
K-Means membantu mengidentifikasi waktu dan kondisi tertentu yang mempengaruhi permintaan sepeda.
