# bike-sharing-analysis-

# 📊 Proyek Analisis Data: Bike Sharing Dataset
##  Informasi
Nama: Shinta Khumaira  
Email: Banoffe1993@gmail.com  
ID Dicoding: maira_14


#  Analisis Data Penyewaan Sepeda (Bike Sharing Dataset)
Proyek ini bertujuan untuk melakukan analisis mendalam terhadap pola penyewaan sepeda berdasarkan faktor waktu (hari kerja vs hari libur) dan kondisi cuaca sepanjang tahun 2011 hingga 2012. Analisis ini mencakup seluruh siklus hidup data, mulai dari pengolahan data mentah (Data Wrangling) hingga pembuatan dashboard interaktif untuk menyajikan temuan bisnis.

# pertanyaan 

Pertanyaan 1: Bagaimana perbedaan pola jumlah penyewaan sepeda per jam antara hari kerja (working day) dan hari libur (non-working day) sepanjang periode 2011-2012?  

Pertanyaan 2: Bagaimana pengaruh variasi kondisi cuaca (weathersit) terhadap rata-rata jumlah penyewaan sepeda harian oleh pengguna tipe Casual dan Registered pada tahun 2012?

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## 📂 Struktur Proyek

submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt


# ▶️ Cara Menjalankan Dashboard (Lokal)

1. Install dependencies:
   pip install -r requirements.txt

2. Jalankan Streamlit:
   python -m streamlit run dashboard.py

3. Buka browser:
http://localhost:8501


## ☁️ Deploy ke Streamlit Cloud

1. Upload project ke GitHub
2. Buka Streamlit Cloud
3. Klik **New App**
4. Pilih repository
5. Masukkan path:
   dashboard/dashboard.py
6. Klik Deploy

## Insight Utama

1: Penyewaan di hari kerja memiliki dua puncak utama (08:00 dan 17:00), menunjukkan penggunaan untuk transportasi. Di hari libur, puncak terjadi di tengah hari (12:00-15:00) yang menunjukkan penggunaan untuk rekreasi.
2: Pengguna registered lebih stabil di berbagai cuaca dibanding pengguna casual yang turun drastis saat cuaca mulai mendung atau hujan ringan. Cuaca cerah memberikan angka tertinggi untuk kedua tipe pengguna.

##  Rekomendasi
Operasional: Pastikan ketersediaan sepeda maksimal di stasiun area perkantoran pada jam 08:00 dan 17:00 di hari kerja.
Marketing: Buat kampanye "Weekend Fun" yang menyasar pengguna casual saat cuaca diprediksi cerah di akhir pekan untuk mendongkrak penjualan.

## Dashboard Online

(Tambahkan link Streamlit Cloud di sini setelah deploy)
