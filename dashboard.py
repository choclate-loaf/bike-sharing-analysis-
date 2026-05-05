import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Dashboard Analisis Sepeda - Shinta Khumaira",
    page_icon="🚲",
    layout="wide"
)

# --- FUNGSI LOAD DATA ---
@st.cache_data
def load_data():
    # Menggunakan path relatif yang lebih aman untuk Streamlit Cloud
    # Mencoba membaca dari folder 'data/' (lokal) atau root (GitHub)
    if os.path.exists('data/day.csv'):
        day_path = 'data/day.csv'
        hour_path = 'data/hour.csv'
    else:
        day_path = 'day.csv'
        hour_path = 'hour.csv'
        
    day_df = pd.read_csv(day_path)
    hour_df = pd.read_csv(hour_path)
    
    # Cleaning: Konversi dteday ke datetime
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    # Mapping untuk label agar lebih informatif
    day_df['season_label'] = day_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    
    return day_df, hour_df

# Memastikan aplikasi tidak crash jika file tidak ditemukan
try:
    day_df, hour_df = load_data()
except FileNotFoundError:
    st.error("Error: File dataset ('day.csv' & 'hour.csv') tidak ditemukan. Pastikan file berada di folder yang sama dengan dashboard.py di GitHub.")
    st.stop()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://static.vecteezy.com/system/resources/previews/000/594/193/original/bicycle-icon-vector-illustration.jpg")
    st.markdown("### Profil Peneliti")
    st.markdown("**Nama:** Shinta Khumaira")
    st.markdown("**Email:** Banoffe1993@gmail.com")
    st.markdown("**ID Dicoding:** maira_14")
    st.markdown("---")
    
    # Filter Tahun
    selected_year = st.selectbox("Pilih Tahun", options=[2011, 2012])
    # yr = 0 adalah 2011, yr = 1 adalah 2012
    year_val = 0 if selected_year == 2011 else 1
    
    # Filter Data berdasarkan tahun
    filtered_day_df = day_df[day_df['yr'] == year_val].copy()

# --- MAIN DASHBOARD ---
st.title("📊 Proyek Analisis Data: Bike Sharing Dataset")
st.markdown(f"Menampilkan analisis untuk tahun **{selected_year}**")

# --- METRIC SECTION ---
st.header("1. Ringkasan Total Penyewa")
col1, col2, col3 = st.columns(3)

with col1:
    total_casual = filtered_day_df['casual'].sum()
    st.metric("Total Pelanggan Kasual", f"{total_casual:,}")

with col2:
    total_registered = filtered_day_df['registered'].sum()
    st.metric("Total Pelanggan Terdaftar", f"{total_registered:,}")

with col3:
    total_cnt = filtered_day_df['cnt'].sum()
    st.metric("Total Keseluruhan", f"{total_cnt:,}")

st.info("💡 **Insight:** Pengguna **terdaftar** (registered) jauh lebih mendominasi dibandingkan pengguna kasual.")

# --- SEASONAL ANALYSIS ---
st.header("2. Kondisi Puncak Peminjaman (Musim)")
fig, ax = plt.subplots(figsize=(10, 5))

# Menggunakan urutan musim yang benar
season_order = ['Spring', 'Summer', 'Fall', 'Winter']
seasonal_usage = filtered_day_df.groupby('season_label')['cnt'].sum().reindex(season_order).reset_index()

sns.barplot(x='season_label', y='cnt', data=seasonal_usage, palette='viridis', ax=ax)
ax.set_title(f"Total Peminjaman Berdasarkan Musim ({selected_year})")
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

st.success("✅ **Hasil Analisis:** Musim **Fall** menunjukkan angka tertinggi secara konsisten.")

# --- TREND ANALYSIS ---
st.header("3. Tren Kinerja Penyewaan (Bulanan)")
fig2, ax2 = plt.subplots(figsize=(12, 5))

monthly_trend = filtered_day_df.groupby('mnth')['cnt'].sum().reset_index()
sns.lineplot(x='mnth', y='cnt', data=monthly_trend, marker='o', color='blue', ax=ax2)

ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
ax2.set_title(f"Tren Peminjaman Bulanan Tahun {selected_year}")
ax2.set_xlabel("Bulan")
ax2.set_ylabel("Jumlah Sewa")
st.pyplot(fig2)

# --- WORKING DAY COMPARISON ---
st.header("4. Perbandingan Hari Kerja vs Hari Libur")
fig3, ax3 = plt.subplots(figsize=(8, 4))

workingday_avg = filtered_day_df.groupby('workingday')['cnt'].mean().reset_index()
workingday_avg['status'] = workingday_avg['workingday'].map({0: 'Hari Libur/Weekend', 1: 'Hari Kerja'})

sns.barplot(x='status', y='cnt', data=workingday_avg, palette='Set2', ax=ax3)
ax3.set_title("Rata-rata Peminjaman Harian")
ax3.set_ylabel("Rata-rata Jumlah Sewa")
st.pyplot(fig3)

st.caption(f"© 2026 Shinta Khumaira | Terakhir diperbarui: {pd.Timestamp.now().strftime('%d %B %Y')}")
