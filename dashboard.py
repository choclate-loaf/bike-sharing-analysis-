import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set judul dashboard
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
st.header('Bike Sharing Analytics Dashboard 🚲')

# Memuat data
@st.cache_data # Menambahkan cache agar loading lebih cepat
def load_data():
    # Pastikan file main_data.csv ada di root folder repository GitHub Anda
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_df = load_data()

# PERBAIKAN: Menghapus spasi di depan (IndentationError fix)
# Filter Rentang Waktu
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
col1, col2 = st.columns(2)
with col1:
    total_rentals = filtered_df['cnt'].sum()
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")
with col2:
    avg_rentals = round(filtered_df['cnt'].mean(), 2)
    st.metric("Rata-rata Penyewaan", value=avg_rentals)

# --- VISUALISASI 1: MUSIM & CUACA ---
st.markdown("---")
st.subheader("Analisis Berdasarkan Musim dan Cuaca")

col_a, col_b = st.columns(2)

with col_a:
    seasonal_counts = filtered_df.groupby('season').cnt.sum().sort_values(ascending=False)
    season_names = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    labels = [season_names[idx] for idx in seasonal_counts.index]
    ax.bar(labels, seasonal_counts.values, color='skyblue', edgecolor='black')
    ax.set_title('Total Rentals by Season')
    st.pyplot(fig)

with col_b:
    weather_counts = filtered_df.groupby('weathersit').cnt.sum().sort_values(ascending=False)
    weather_names = {1: 'Clear', 2: 'Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain'}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    labels = [weather_names.get(idx, 'Other') for idx in weather_counts.index]
    ax.bar(labels, weather_counts.values, color='lightcoral', edgecolor='black')
    ax.set_title('Total Rentals by Weather')
    st.pyplot(fig)

# --- VISUALISASI 2: REGISTERED VS CASUAL ---
st.markdown("---")
st.subheader("Registered vs Casual Customers")

# Menggunakan freq='ME' untuk Monthly End
monthly_rentals = filtered_df.groupby(pd.Grouper(key='dteday', freq='ME')).agg({
    "casual": "sum",
    "registered": "sum"
}).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_rentals['dteday'], monthly_rentals['registered'], marker='o', label='Registered', color='#72BCD4')
ax.plot(monthly_rentals['dteday'], monthly_rentals['casual'], marker='o', label='Casual', color='#D3D3D3')
ax.set_title('Monthly Trends: Registered vs Casual')
ax.legend()
st.pyplot(fig)

# Pie Chart
st.write("#### User Composition")
total_reg = filtered_df['registered'].sum()
total_cas = filtered_df['casual'].sum()

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie([total_reg, total_cas], labels=['Registered', 'Casual'], autopct='%1.1f%%', colors=['#72BCD4', '#D3D3D3'], startangle=90)
ax.set_title('User Composition')
st.pyplot(fig)

st.caption('Copyright (c) Shinta Khumaira 2026')
