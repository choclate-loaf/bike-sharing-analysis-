import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("🚲 Dashboard Penyewaan Sepeda")

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    
    # Cleaning: Konversi tipe data tanggal
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    # Mapping label cuaca untuk visualisasi
    weather_map = {1: 'Cerah/Berawan', 2: 'Mendung/Kabut', 3: 'Hujan/Salju Ringan', 4: 'Hujan Lebat'}
    day_df['weather_label'] = day_df['weathersit'].map(weather_map)
    
    return day_df, hour_df

# Memanggil data
day_df, hour_df = load_data()

# --- SIDEBAR ---
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    st.image("https://raw.githubusercontent.com/dicodingacademy/dicoding-main-repo/main/Assets/logo_dicoding.png")
    
    # Filter rentang waktu
    try:
        start_date, end_date = st.date_input(
            label='Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
    except:
        start_date, end_date = min_date, max_date

# Filter data berdasarkan sidebar
main_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                (day_df["dteday"] <= pd.to_datetime(end_date))]

main_hour_df = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & 
                      (hour_df["dteday"] <= pd.to_datetime(end_date))]

# --- MAIN PAGE ---
# 1. Ringkasan Statistik (Matriks)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=f"{main_df.cnt.sum():,}")
with col2:
    st.metric("Pengguna Registered", value=f"{main_df.registered.sum():,}")
with col3:
    st.metric("Pengguna Casual", value=f"{main_df.casual.sum():,}")

st.divider()

# 2. Visualisasi Tren Per Jam (Hari Kerja vs Libur)
st.subheader("📈 Pola Penyewaan Per Jam: Hari Kerja vs Hari Libur")
hourly_rentals = main_hour_df.groupby(['workingday', 'hr'])['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=hourly_rentals, x='hr', y='cnt', hue='workingday', marker='o', palette='tab10', ax=ax)
ax.set_xlabel("Jam (0-23)")
ax.set_ylabel("Rata-rata Sewa")
ax.legend(title='Tipe Hari', labels=['Hari Libur / Akhir Pekan', 'Hari Kerja'])
st.pyplot(fig)

with st.expander("Lihat Detail Analisis Tren Jam"):
    st.write("Penyewaan pada hari kerja memiliki dua puncak utama yaitu jam 08:00 dan 17:00. Sebaliknya, hari libur mencapai puncak di tengah hari.")

# 3. Visualisasi Dampak Cuaca
st.subheader("☁️ Dampak Kondisi Cuaca terhadap Tipe Pengguna")
df_weather = main_df.groupby('weather_label')[['casual', 'registered']].mean().reset_index()
weather_melted = df_weather.melt(id_vars='weather_label', value_vars=['casual', 'registered'], 
                                 var_name='Tipe Pengguna', value_name='Rata-rata Penyewaan')

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=weather_melted, x='weather_label', y='Rata-rata Penyewaan', hue='Tipe Pengguna', palette='Set2', ax=ax2)
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Rata-rata Jumlah Sewa")
st.pyplot(fig2)

st.caption('Copyright (C) 2026 - Shinta Khumaira')