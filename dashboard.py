import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set judul dashboard
st.header('Bike Sharing Analytics Dashboard 🚲')

# Memuat data
@st.cache_data 
def load_data():
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_df = load_data()

# PERBAIKAN 1: Indentasi diperbaiki (start_date disejajarkan ke kiri)
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
    st.metric("Rata-rata Penyewaan/Jam", value=avg_rentals)

# --- VISUALISASI 1: MUSIM & CUACA ---
st.subheader("Analisis Berdasarkan Musim dan Cuaca")

# Musim
seasonal_counts = filtered_df.groupby('season').cnt.sum().sort_values(ascending=False)
season_names = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
season_colors = {'Winter': 'lightblue', 'Spring': 'lightgreen', 'Summer': 'lightyellow', 'Fall': 'pink'}

labels = [season_names[idx] for idx in seasonal_counts.index]
sizes = seasonal_counts.values
colors = [season_colors[label] for label in labels]

fig1, ax1 = plt.subplots(figsize=(10, 6)) # PERBAIKAN 2: Menggunakan subplots
ax1.bar(labels, sizes, color=colors, edgecolor='black')
ax1.set_xlabel('Season')
ax1.set_ylabel('Total Rentals')
ax1.set_title('Total Bike Rentals by Season')
for i, value in enumerate(sizes):
    ax1.text(i, value + 500, str(value), ha='center', va='bottom')
st.pyplot(fig1) # PERBAIKAN 3: Menampilkan di Streamlit

# Cuaca
weather_counts = filtered_df.groupby('weathersit').cnt.sum().sort_values(ascending=False)
weather_names = {1: 'Clear', 2: 'Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Ice Pallets'}
weather_colors = {'Clear':'skyblue', 'Cloudy':'lightblue', 'Light Snow/Rain':'grey', 'Heavy Rain/Ice Pallets':'white'}

labels_w = [weather_names[idx] for idx in weather_counts.index]
colors_weather = [weather_colors[label] for label in labels_w]

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(labels_w, weather_counts.values, color=colors_weather, edgecolor='black')
ax2.set_xlabel('Weather')
ax2.set_ylabel('Total Rentals')
ax2.set_title('Total Bike Rentals by Weather')
for i, value in enumerate(weather_counts.values):
    ax2.text(i, value + 500, str(value), ha='center', va='bottom')
st.pyplot(fig2)

# Waktu (Hourly)
hourly_counts = filtered_df.groupby('hr')['cnt'].sum()
fig3, ax3 = plt.subplots(figsize=(10, 6))
hourly_counts.plot(kind='bar', color='lightblue', ax=ax3)
ax3.set_title('Total Bike Rentals by Hour of the Day')
ax3.set_xlabel('Hour')
ax3.set_ylabel('Total Rentals')
st.pyplot(fig3)

# Heatmap
clustering = filtered_df.groupby(['weekday', 'hr'])['cnt'].sum().unstack()
fig4, ax4 = plt.subplots(figsize=(12, 8))
sns.heatmap(clustering, cmap="coolwarm", annot=False, fmt=".0f", ax=ax4)
ax4.set_title('Bike Rentals Heatmap by Weekday and Hour')
st.pyplot(fig4)

# --- VISUALISASI 2: REGISTERED VS CASUAL ---
st.subheader("Registered vs Casual Customers")

# PERBAIKAN 4: Menghapus baris day_df yang menyebabkan error
monthly_rentals = filtered_df.groupby(pd.Grouper(key='dteday', freq='ME')).agg({
    "casual": "sum",
    "registered": "sum"
}).reset_index()

fig5, ax5 = plt.subplots(figsize=(14, 8))
ax5.plot(monthly_rentals['dteday'], monthly_rentals['registered'], marker='o', label='Registered Rentals')
ax5.plot(monthly_rentals['dteday'], monthly_rentals['casual'], marker='o', label='Casual Rentals')
ax5.set_title('Monthly Bike Rentals of Registered and Casual Customers')
ax5.legend()
plt.xticks(rotation=45)
st.pyplot(fig5)

# Pie Chart
total_registered = filtered_df['registered'].sum()
total_casual = filtered_df['casual'].sum()
fig6, ax6 = plt.subplots(figsize=(8, 6))
ax6.pie([total_registered, total_casual], labels=['Registered', 'Casual'], colors=['lightblue', 'white'], autopct='%1.1f%%', startangle=140)
ax6.set_title('Percentage of Registered vs Casual Customer')
st.pyplot(fig6)

st.caption('Copyright (c) Shinta Khumaira 2026')
