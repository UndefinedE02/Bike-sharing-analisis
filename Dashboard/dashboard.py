import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load dataset
path_data = os.path.join(os.path.dirname(__file__), "main_data.csv")
imple_data = pd.read_csv(path_data)

# Pilih fitur untuk clustering
fitur = ['temp', 'hum', 'windspeed', 'hr']

# Mengisi NaN dengan nilai rata-rata
imputer = SimpleImputer(strategy='mean')
data_imputed = imputer.fit_transform(imple_data[fitur])

# Standarisasi data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_imputed)

# Tentukan jumlah cluster
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Lakukan clustering
imple_data['cluster'] = kmeans.fit_predict(data_scaled)

# Sidebar
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", ["Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"])
selected_weekday = st.sidebar.selectbox("Pilih Hari", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])

# Mapping
season_mapping = {"Musim Semi": 1, "Musim Panas": 2, "Musim Gugur": 3, "Musim Dingin": 4}
weekday_mapping = {"Senin": 0, "Selasa": 1, "Rabu": 2, "Kamis": 3, "Jumat": 4, "Sabtu": 5, "Minggu": 6}

# Filter data
df_filtered = imple_data[(imple_data['season'] == season_mapping[selected_season]) & 
                    (imple_data['weekday'] == weekday_mapping[selected_weekday])]

st.title("Dashboard Bike Sharing Analysis")
st.write("### Tren Penggunaan Sepeda Berdasarkan Waktu")

# Visualisasi berdasarkan waktu
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=df_filtered['hr'], y=df_filtered['cnt'], ax=ax)
plt.xlabel("Jam")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.write("### Hubungan Cuaca dan Penggunaan Sepeda")

# Scatter plot suhu
fig, ax = plt.subplots(figsize=(6, 4))
sns.scatterplot(x=df_filtered['temp'], y=df_filtered['cnt'], ax=ax)
plt.xlabel("Suhu")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Clustering Visualisasi
st.write("### Hasil Clustering Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=df_filtered['temp'], y=df_filtered['cnt'], hue=df_filtered['cluster'], palette='viridis', ax=ax)
plt.xlabel("Suhu")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)
