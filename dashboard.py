import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set judul dashboard
st.header('Bike Sharing Analytics Dashboard 🚲')

# Memuat data yang sudah disimpan tadi
def load_data():
    df = pd.read_csv("dashboard/main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_df = load_data()

# Menambahkan filter di Sidebar
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png") # Opsional: Logo
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
    st.metric("Total Penyewaan", value=total_rentals)
with col2:
    avg_rentals = round(filtered_df['cnt'].mean(), 2)
    st.metric("Rata-rata Penyewaan/Jam", value=avg_rentals)

# Visualisasi 1: Berdasarkan Jam (Dari EDA di notebook Anda)
st.subheader("Tren Penyewaan Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(16, 8))
sns.lineplot(x="hr", y="cnt", data=filtered_df, marker='o', ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah")
st.pyplot(fig)

# Visualisasi 2: Registered vs Casual (Pertanyaan 1 Anda)
st.subheader("Perbandingan Pengguna Registered vs Casual")
fig, ax = plt.subplots(figsize=(10, 6))
labels = ['Registered', 'Casual']
sizes = [filtered_df['registered'].sum(), filtered_df['casual'].sum()]
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#72BCD4', '#D3D3D3'])
st.pyplot(fig)

st.caption('Copyright (c) Shinta Khumaira 2026')