import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set judul dashboard
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
st.header('Bike Sharing Analytics Dashboard 🚲')

# Memuat data bersih
@st.cache_data 
def load_data():
    df = pd.read_csv("main_data.csv") 
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_df = load_data()

# Sidebar untuk filter rentang waktu
with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=main_df['dteday'].min(),
        max_value=main_df['dteday'].max(),
        value=[main_df['dteday'].min(), main_df['dteday'].max()]
    )

# Filter data berdasarkan input user
filtered_df = main_df[(main_df['dteday'] >= pd.to_datetime(start_date)) & 
                       (main_df['dteday'] <= pd.to_datetime(end_date))]

# Menampilkan Metric Utama
col1, col2, col3 = st.columns(3)
with col1:
    total_rentals = filtered_df['cnt'].sum()
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")
with col2:
    total_registered = filtered_df['registered'].sum()
    st.metric("Pelanggan Terdaftar", value=f"{total_registered:,}")
with col3:
    total_casual = filtered_df['casual'].sum()
    st.metric("Pelanggan Casual", value=f"{total_casual:,}")

st.divider()

# --- VISUALISASI 1: MUSIM & CUACA ---
st.subheader("Faktor Eksternal: Musim dan Cuaca")

col_a, col_b = st.columns(2)

with col_a:
    # Menggunakan season_desc dari main_data.csv
    seasonal_counts = filtered_df.groupby('season_desc').cnt.sum().sort_values(ascending=False)
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=seasonal_counts.index, y=seasonal_counts.values, palette="viridis", ax=ax1)
    ax1.set_title('Penyewaan Berdasarkan Musim')
    ax1.set_ylabel('Total Penyewaan')
    ax1.set_xlabel(None)
    st.pyplot(fig1)

with col_b:
    # Menggunakan weather_desc dari main_data.csv
    weather_counts = filtered_df.groupby('weather_desc').cnt.sum().sort_values(ascending=False)
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=weather_counts.index, y=weather_counts.values, palette="magma", ax=ax2)
    ax2.set_title('Penyewaan Berdasarkan Kondisi Cuaca')
    ax2.set_ylabel('Total Penyewaan')
    ax2.set_xlabel(None)
    st.pyplot(fig2)

# --- VISUALISASI 2: TREN BULANAN ---
st.subheader("Tren Penyewaan Bulanan (Registered vs Casual)")

monthly_rentals = filtered_df.resample(rule='M', on='dteday').agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
}).reset_index()

fig3, ax3 = plt.subplots(figsize=(16, 8))
ax3.plot(monthly_rentals['dteday'], monthly_rentals['registered'], marker='o', linewidth=2, label='Registered', color='#2E86C1')
ax3.plot(monthly_rentals['dteday'], monthly_rentals['casual'], marker='o', linewidth=2, label='Casual', color='#E67E22')
ax3.set_title('Tren Penyewaan Sepeda per Bulan', fontsize=20)
ax3.legend(fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig3)

# --- VISUALISASI 3: PERBANDINGAN KOMPOSISI ---
st.subheader("Komposisi Pelanggan")

fig4, ax4 = plt.subplots(figsize=(8, 8))
labels = ['Registered', 'Casual']
sizes = [total_registered, total_casual]
colors = ['#2E86C1', '#E67E22']
ax4.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=(0.1, 0))
ax4.set_title('Perbandingan Total Pelanggan')
st.pyplot(fig4)

st.caption('Copyright (c) Shinta Khumaira 2026 | Data Source: main_data.csv')
