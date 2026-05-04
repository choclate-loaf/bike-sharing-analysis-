import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set judul dashboard
st.header('Bike Sharing Analytics Dashboard 🚲')

# Memuat data yang sudah disimpan tadi
def load_data():
    df = pd.read_csv("main_data.csv")
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

# Visualisasi 1: 
# Musim
seasonal_counts = main_df.groupby('season').cnt.sum().sort_values(ascending=False)

# Create a mapping for season numbers to names
season_names = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}

season_colors = {
    'Winter': 'lightblue',
    'Spring': 'lightgreen',
    'Summer': 'lightyellow',
    'Fall': 'pink'  # Changed 'babypink' to 'pink'
}

plt.figure(figsize=(8, 6))

# Map numerical season labels to descriptive names
labels = [season_names[idx] for idx in seasonal_counts.index]
sizes = seasonal_counts.values
colors = [season_colors[label] for label in labels]

plt.figure(figsize=(10, 6))
plt.bar(labels, sizes, color=colors, edgecolor='black')

plt.xlabel('Season')
plt.ylabel('Total Rentals')
plt.title('Total Bike Rentals by Season')
for i, value in enumerate(sizes):
    plt.text(i, value + 500, str(value), ha='center', va='bottom')
plt.tight_layout()
plt.show()

#Cuaca
weather_counts = main_df.groupby('weathersit').cnt.sum().sort_values(ascending=False)

# Create a mapping for weathersit numbers to names
weather_names = {
    1: 'Clear',
    2: 'Cloudy',
    3: 'Light Snow/Rain',
    4: 'Heavy Rain/Ice Pallets'
}

weather_colors = {
    'Clear':'skyblue',
    'Cloudy':'lightblue',
    'Light Snow/Rain':'grey',
    'Heavy Rain/Ice Pallets':'white'
}

sizes = weather_counts.values
# Map numerical weathersit labels to descriptive names
labels = [weather_names[idx] for idx in weather_counts.index]
colors_weather = [weather_colors[label] for label in labels]

plt.figure(figsize=(10, 6))
plt.bar(labels, sizes, color=colors_weather, edgecolor='black')

plt.xlabel('Weather')
plt.ylabel('Total Rentals')
plt.title('Total Bike Rentals by Weather')
for i, value in enumerate(sizes):
    plt.text(i, value + 500, str(value), ha='center', va='bottom')
plt.tight_layout()
plt.show()

# Waktu
hourly_counts = main_df.groupby('hr')['cnt'].sum()

plt.figure(figsize=(10, 6))
hourly_counts.plot(kind='bar', color='lightblue')
plt.title('Total Bike Rentals by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Total Rentals')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

clustering = main_df.groupby(['weekday', 'hr'])['cnt'].sum().unstack()

print(clustering)

plt.figure(figsize=(12, 8))
sns.heatmap(clustering, cmap="coolwarm", annot=False, fmt=".0f")
plt.title('Bike Rentals Heatmap by Weekday and Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.show()



# Visualisasi 2: Registered vs Casual (Pertanyaan 1 Anda)
monthly_rentals = day_df.groupby(pd.Grouper(key='dteday', freq='ME')).agg({
    "casual": "sum",
    "registered": "sum"
}).reset_index()
monthly_rentals = monthly_rentals.rename(columns={'dteday': 'date'})

plt.figure(figsize=(14, 8))
plt.plot(monthly_rentals['date'], monthly_rentals['registered'], marker='o', label='Registered Rentals')
plt.plot(monthly_rentals['date'], monthly_rentals['casual'], marker='o', label='Casual Rentals')

plt.title('Monthly Bike Rentals of Registered and Casual Customers')
plt.xlabel('Month')
plt.ylabel('Total Customers')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

plt.show()

total_registered = main_df['registered'].sum()
total_casual = main_df['casual'].sum()
labels = ['Registered', 'Casual']
sizes = [total_registered, total_casual]
colors = ['lightblue', 'white']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)
plt.axis('equal')
plt.title('Percentage of Registered vs Casual Customer')
plt.tight_layout()
plt.show()



st.caption('Copyright (c) Shinta Khumaira 2026')