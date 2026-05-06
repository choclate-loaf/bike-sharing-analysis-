import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- KONFIGURASI ---
sns.set_style("whitegrid")

PRIMARY_COLOR = "#92c9e9"
SECONDARY_COLOR = "#c43aad"
ACCENT_COLOR_DARK = "#d62728"
ACCENT_COLOR_LIGHT = "#aec7e8"

st.set_page_config(
    page_title="Dashboard Peminjaman Sepeda",
    page_icon="🚲",
    layout="wide"
)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    try:
        hour_df = pd.read_csv('hour.csv')
        day_df = pd.read_csv('day.csv')
    except FileNotFoundError:
        hour_df = pd.read_csv('hour.csv')
        day_df = pd.read_csv('day.csv')

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    return day_df, hour_df


def style_plot(ax, title, xlabel, ylabel, rotation=0):
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.tick_params(axis='x', rotation=rotation)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=10)


main_day_df, main_hour_df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("**Nama:** Shinta Khumaira")
    st.markdown("**Email:** Banoffe1993@gmail.com")
    st.markdown("**ID Dicoding:** maira_14")
    st.markdown("---")

    st.header("⚙️ Filter Data")

    selected_season = st.selectbox(
        "Pilih Musim",
        ["Semua", "Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"]
    )

    selected_years = st.multiselect(
        "Pilih Tahun",
        options=[2011, 2012],
        default=[2011, 2012]
    )

    selected_weathers = st.multiselect(
        "Pilih Kondisi Cuaca",
        options=["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras"],
        default=["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras"]
    )

# --- FILTER DATA ---
day_df = main_day_df.copy()
hour_df = main_hour_df.copy()

if selected_season != "Semua":
    season_map = {"Musim Semi": 1, "Musim Panas": 2, "Musim Gugur": 3, "Musim Dingin": 4}
    day_df = day_df[day_df['season'] == season_map[selected_season]]
    hour_df = hour_df[hour_df['season'] == season_map[selected_season]]

if selected_years:
    year_map = {2011: 0, 2012: 1}
    selected_year_values = [year_map[y] for y in selected_years]
    day_df = day_df[day_df['yr'].isin(selected_year_values)]
    hour_df = hour_df[hour_df['yr'].isin(selected_year_values)]

if selected_weathers:
    weather_map = {"Cerah": 1, "Berawan": 2, "Hujan Ringan": 3, "Hujan Deras": 4}
    selected_weather_values = [weather_map[w] for w in selected_weathers]
    day_df = day_df[day_df['weathersit'].isin(selected_weather_values)]
    hour_df = hour_df[hour_df['weathersit'].isin(selected_weather_values)]

# --- HEADER ---
st.title("📊 Dashboard Analisis Peminjaman Sepeda")
st.markdown("---")

if day_df.empty or hour_df.empty:
    st.warning("Data kosong, ubah filter.")
else:

    tab1, tab2, tab3, tab4 = st.tabs([
        "👥 Perbandingan Pengguna",
        "🚀 Pertumbuhan Bulanan",
        "📈 Fluktuasi Tahunan",
        "⏰ Pola Penggunaan Harian"
    ])

    # TAB 1
    with tab1:
        st.header("Perbandingan Pengguna")

        monthly_users = day_df.groupby('mnth')[['casual', 'registered']].sum()
        monthly_users = monthly_users.rename(columns={
            'casual': 'Kasual',
            'registered': 'Terdaftar'
        })

        fig, ax = plt.subplots(figsize=(12, 6))
        monthly_users.plot(kind='bar',
                           color=[PRIMARY_COLOR, SECONDARY_COLOR],
                           ax=ax)

        ax.axhline(monthly_users['Kasual'].mean(), linestyle='--')
        ax.axhline(monthly_users['Terdaftar'].mean(), linestyle='--')

        style_plot(ax, 'Jumlah Pengguna per Bulan', 'Bulan', 'Jumlah')
        st.pyplot(fig)

    # TAB 2
    with tab2:
        st.header("Pertumbuhan Bulanan")

        monthly_growth = day_df.groupby('mnth')[['casual', 'registered']].sum().pct_change() * 100

        fig, ax = plt.subplots(figsize=(12, 6))

        ax.bar(monthly_growth.index, monthly_growth['casual'], label='Kasual')
        ax.bar(monthly_growth.index, monthly_growth['registered'], label='Terdaftar')

        style_plot(ax, 'Pertumbuhan (%)', 'Bulan', '%')
        st.pyplot(fig)

    # TAB 3
    with tab3:
        st.header("Fluktuasi Tahunan")

        monthly_trends = day_df.groupby('mnth')[['casual', 'registered']].sum()

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(monthly_trends.index, monthly_trends['casual'], marker='o')
        ax.plot(monthly_trends.index, monthly_trends['registered'], marker='o')

        style_plot(ax, 'Tren Tahunan', 'Bulan', 'Jumlah')
        st.pyplot(fig)

    # TAB 4
    with tab4:
        st.header("Pola Jam Harian")

        hourly = hour_df.groupby('hr')['cnt'].mean().reset_index()

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=hourly, x='hr', y='cnt', marker='o', ax=ax)

        ax.fill_between(hourly['hr'], hourly['cnt'], alpha=0.2)

        ax.axvspan(7, 9, color='orange', alpha=0.2)
        ax.axvspan(16, 19, color='red', alpha=0.2)

        style_plot(ax, 'Pola Jam Sibuk', 'Jam', 'Jumlah')
        st.pyplot(fig)

# FOOTER
st.markdown("---")
st.caption("© 2026 Shinta Khumaira")