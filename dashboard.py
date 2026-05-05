import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- STYLE ---
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
    except:
        hour_df = pd.read_csv('../data/hour.csv')
        day_df = pd.read_csv('../data/day.csv')

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    return day_df, hour_df

def style_plot(ax, title, xlabel, ylabel, rotation=0):
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis='x', rotation=rotation)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    if ax.get_legend_handles_labels()[0]:
        ax.legend()

# --- DATA ---
main_day_df, main_hour_df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("**Nama:** Shinta Khumaira")
    st.markdown("**Email:** Banoffe1993@gmail.com")
    st.markdown("---")

    st.header("Filter")

    selected_season = st.selectbox(
        "Pilih Musim",
        ["Semua", "Musim Semi", "Musim Panas", "Musim Gugur", "Musim Dingin"]
    )

    selected_years = st.multiselect(
        "Pilih Tahun",
        [2011, 2012],
        default=[2011, 2012]
    )

    selected_weathers = st.multiselect(
        "Cuaca",
        ["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras"],
        default=["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras"]
    )

# --- FILTER ---
day_df = main_day_df.copy()
hour_df = main_hour_df.copy()

if selected_season != "Semua":
    season_map = {"Musim Semi": 1, "Musim Panas": 2, "Musim Gugur": 3, "Musim Dingin": 4}
    day_df = day_df[day_df['season'] == season_map[selected_season]]
    hour_df = hour_df[hour_df['season'] == season_map[selected_season]]

if selected_years:
    year_map = {2011: 0, 2012: 1}
    vals = [year_map[y] for y in selected_years]
    day_df = day_df[day_df['yr'].isin(vals)]
    hour_df = hour_df[hour_df['yr'].isin(vals)]

if selected_weathers:
    weather_map = {"Cerah": 1, "Berawan": 2, "Hujan Ringan": 3, "Hujan Deras": 4}
    vals = [weather_map[w] for w in selected_weathers]
    day_df = day_df[day_df['weathersit'].isin(vals)]
    hour_df = hour_df[hour_df['weathersit'].isin(vals)]

# --- TITLE ---
st.title("📊 Dashboard Analisis Peminjaman Sepeda")
st.markdown("---")

if day_df.empty or hour_df.empty:
    st.warning("Data kosong, ubah filter.")
else:
    tab1, tab2, tab3, tab4 = st.tabs([
        "👥 Perbandingan",
        "📈 Growth",
        "📊 Tren",
        "⏰ Jam Sibuk"
    ])

    # TAB 1
    with tab1:
        monthly = day_df.groupby('mnth')[['casual', 'registered']].sum()
        monthly.columns = ['Kasual', 'Terdaftar']

        fig, ax = plt.subplots(figsize=(12, 6))
        monthly.plot(kind='bar', color=[PRIMARY_COLOR, SECONDARY_COLOR], ax=ax, edgecolor='black')

        ax.axhline(monthly['Kasual'].mean(), color=PRIMARY_COLOR, linestyle='--')
        ax.axhline(monthly['Terdaftar'].mean(), color=SECONDARY_COLOR, linestyle='--')

        style_plot(ax, "Pengguna per Bulan", "Bulan", "Jumlah")
        st.pyplot(fig)

    # TAB 2
    with tab2:
        growth = day_df.groupby('mnth')[['casual', 'registered']].sum().pct_change().fillna(0) * 100

        fig, ax = plt.subplots(figsize=(12, 6))
        x = np.arange(len(growth))

        ax.bar(x - 0.2, growth['casual'], width=0.4, color=ACCENT_COLOR_LIGHT)
        ax.bar(x + 0.2, growth['registered'], width=0.4, color=SECONDARY_COLOR)

        ax.axhline(0, color='black', linestyle='--')
        ax.set_xticks(x)
        ax.set_xticklabels(growth.index)

        style_plot(ax, "Growth (%)", "Bulan", "Persen")
        st.pyplot(fig)

    # TAB 3
    with tab3:
        trend = day_df.groupby('mnth')[['casual', 'registered']].sum()

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(trend.index, trend['casual'], marker='o', color=PRIMARY_COLOR)
        ax.plot(trend.index, trend['registered'], marker='o', color=SECONDARY_COLOR)

        style_plot(ax, "Tren Tahunan", "Bulan", "Jumlah")
        st.pyplot(fig)

    # TAB 4
    with tab4:
        hourly = hour_df.groupby('hr')['cnt'].mean().reset_index()

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=hourly, x='hr', y='cnt', marker='o', color='teal', ax=ax)

        ax.fill_between(hourly['hr'], hourly['cnt'], color='teal', alpha=0.1)
        ax.axvspan(7, 9, color='orange', alpha=0.2)
        ax.axvspan(16, 19, color='red', alpha=0.2)

        style_plot(ax, "Pola Jam Sibuk", "Jam", "Rata-rata Sewa")
        ax.set_xticks(range(0, 24))

        st.pyplot(fig)

# FOOTER
st.markdown("---")
st.caption("© 2026 Shinta Khumaira")