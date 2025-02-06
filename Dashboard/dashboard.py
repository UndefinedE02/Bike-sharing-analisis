import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.impute import SimpleImputer

# Load dataset
path_data = os.path.join(os.path.dirname(__file__), "main_data.csv")
imple_data = pd.read_csv(path_data)

# Pilih fitur yang akan digunakan untuk binning
fitur = ['temp', 'hum', 'windspeed', 'weekday']

# Mengisi NaN dengan nilai rata-rata
imputer = SimpleImputer(strategy='mean')
imple_data[fitur] = imputer.fit_transform(imple_data[fitur])

# **Menggunakan Binning untuk Clustering**
bins = [imple_data['cnt'].min(), 500, 1500, 3000, imple_data['cnt'].max()]
labels = ['Sangat Rendah', 'Rendah', 'Sedang', 'Tinggi']
imple_data['cluster'] = pd.cut(imple_data['cnt'], bins=bins, labels=labels, include_lowest=True)

# Sidebar
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", ["All Season", "Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"])
selected_weekday = st.sidebar.selectbox("Pilih Hari", ["All Day", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])

# Mapping musim & hari
season_mapping = {"Musim Semi": 1, "Musim Panas": 2, "Musim Gugur": 3, "Musim Dingin": 4}
weekday_mapping = {"Senin": 0, "Selasa": 1, "Rabu": 2, "Kamis": 3, "Jumat": 4, "Sabtu": 5, "Minggu": 6}

# **Filter data dengan opsi "All Season" & "All Day"**
if selected_season != "All Season":
    imple_data = imple_data[imple_data['season'] == season_mapping[selected_season]]

if selected_weekday != "All Day":
    imple_data = imple_data[imple_data['weekday'] == weekday_mapping[selected_weekday]]

st.title("Dashboard Bike Sharing Analysis")

st.write("### Hubungan Cuaca dan Penggunaan Sepeda")

# **Scatter plot cuaca vs jumlah peminjaman**
# **Visualisasi Binning (Cluster)**
st.write("### 1. Penggunaan Sepeda Berdasarkan Suhu")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=imple_data['temp'], y=imple_data['cnt'], hue=imple_data['cluster'], palette='viridis', ax=ax)
plt.xlabel("Suhu")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("### 2. Penggunaan Sepeda Berdasarkan Kelembaban")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=imple_data['hum'], y=imple_data['cnt'], hue=imple_data['cluster'], palette='viridis', ax=ax)
plt.xlabel("Kelembaban")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("### 3. Penggunaan Sepeda Berdasarkan kecepatan angin")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=imple_data['windspeed'], y=imple_data['cnt'], hue=imple_data['cluster'], palette='viridis', ax=ax)
plt.xlabel("Kecepatan angin")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("### Tren Penggunaan Sepeda Berdasarkan Waktu")

# **Visualisasi berdasarkan hari**
# Mapping angka ke nama hari
hari_labels = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

# Visualisasi berdasarkan hari
fig, ax = plt.subplots(figsize=(7, 5))
sns.lineplot(x=imple_data['weekday'], y=imple_data['cnt'], ax=ax)

# Ganti label sumbu X menjadi nama hari
ax.set_xticks(range(7))  # Pastikan angka 0-6 ada di sumbu X
ax.set_xticklabels(hari_labels)

plt.xlabel("Hari")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)
