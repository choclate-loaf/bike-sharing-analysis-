import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
st.header('Bike Sharing Analytics Dashboard 🚲')

# Memuat data dengan penanganan error kolom
@st.cache_data 
def load_data():
    df = pd.read_csv("main_data.csv") 
    df['dteday'] = pd.to_datetime(df['dteday'])
    
    # Memastikan kolom deskripsi ada (antisipasi jika tidak sengaja terhapus)
    if 'season_desc' not in df.columns:
        season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
        df['season_desc'] = df['season'].map(season_map)
    if 'weather_desc' not in df.columns:
        weather_map = {1: 'Clear', 2: 'Cloudy', 3: 'Light Rain', 4: 'Heavy Rain'}
        df['weather_desc'] = df['weathersit'].map(weather_map)
        
    return df

main_df = load_data()

# Sidebar
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    # Penyesuaian rentang waktu sesuai data notebook 2011-2012
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=main_df['dteday'].min(),
        max_value=main_df['dteday'].max(),
        value=[main_df['dteday'].min(), main_df['dteday'].max()]
    )

# Filter Data
filtered_df = main_df[(main_df['dteday'] >= pd.to_datetime(start_date)) & 
                       (main_df['dteday'] <= pd.to_datetime(end_date))]

# Metrics Row
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=f"{filtered_df['cnt'].sum():,}")
with col2:
    st.metric("Pelanggan Terdaftar", value=f"{filtered_df['registered'].sum():,}")
with col3:
    st.metric("Pelanggan Casual", value=f"{filtered_df['casual'].sum():,}")

st.divider()

# --- Visualisasi Utama ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Penyewaan Berdasarkan Musim")
    # Grouping menggunakan kolom deskripsi yang sudah divalidasi
    seasonal_data = filtered_df.groupby('season_desc')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=seasonal_data, x='season_desc', y='cnt', palette="Blues_d", ax=ax)
    ax.set_xlabel(None)
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

with col_right:
    st.subheader("Penyewaan Berdasarkan Cuaca")
    weather_data = filtered_df.groupby('weather_desc')['cnt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=weather_data, x='weather_desc', y='cnt', palette="Reds_d", ax=ax)
    ax.set_xlabel(None)
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# --- Tren Bulanan ---
st.subheader("Tren Penyewaan Bulanan")
monthly_trend = filtered_df.resample(rule='M', on='dteday').agg({
    "registered": "sum",
    "casual": "sum"
}).reset_index()

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(monthly_trend['dteday'], monthly_trend['registered'], label='Registered', marker='o', linewidth=2)
ax.plot(monthly_trend['dteday'], monthly_trend['casual'], label='Casual', marker='o', linewidth=2)
ax.set_title("Perkembangan Penyewaan 2011-2012", fontsize=15)
ax.legend()
st.pyplot(fig)

st.caption('Copyright (c) Shinta Khumaira 2026 | Dataset: Bike Sharing - main_data.csv')
