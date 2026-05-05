# Proyek Analisis Data: Bike Sharing Dataset

"Halo! Ini adalah proyek analisis data Bike Sharing saya. Di sini, saya mengeksplorasi pola penyewaan sepeda dan mengemas temuannya ke dalam dasbor web interaktif yang dibuat dengan Streamlit."

## Profil Pengembang
- **Nama:** Shinta Khumaira
- **Email:** Banoffe1993@gmail.com
- **ID Dicoding:** maira_14

##  Dashboard
 visual dapat dilihat langsung: [text](https://bagxusfe2vsmuxjg2npjjf.streamlit.app/)

## Background
Sumber Data: Capital Bikeshare, Washington D.C. (2011-2012).

Variabel: Waktu (jam/hari), lingkungan (cuaca/musim), dan tipe pengguna.

Manfaat: Optimasi bisnis dan efisiensi strategi pemasaran.

## Pertanyaan Bisnis 
### Pertanyaan 1:  Bagaimana komparasi tren volume pengguna casual dan pengguna registered pada setiap bulannya?
### Pertanyaan 2: : pada bulan apa terjadi kenaikan jumlah pengguna casual dan registered paling besar dibandingkan dengan periode bulan sebelumnya?"
### pertanyaan 3: Analisis fluktuasi tahunan: Bagaimana perbandingan pola pertumbuhan antara pengguna casual dan registered dari bulan ke bulan?"
### Pertanyaan 4: Bagaimana pola penyewaan sepeda sepanjang hari, khususnya saat membandingkan jam sibuk dengan jam tidak sibuk? Selain itu, faktor eksternal apa saja yang memengaruhi perbedaan volume penggunaan tersebut?"

##  Fitur Dasbor
Filter Data Dinamis: Pengguna dapat memfilter data berdasarkan:
* Rentang Tanggal
* Musim (Semi, Panas, Gugur, Dingin)
* Tahun (2011, 2012)
* Kondisi Cuaca (Cerah, Berawan, Hujan * Ringan, Hujan Deras)

### Analisis disajikan dalam empat tab terpisah untuk fokus pada setiap pertanyaan bisnis.


## Teknologi yang Digunakan
* Analisis Data: Python, Pandas, NumPy
* Visualisasi Data: Matplotlib, Seaborn
* Dashboard Interaktif: Streamlit



Isi File README.md
Markdown
# Proyek Analisis Data: Bike Sharing Dataset

Proyek ini bertujuan untuk melakukan analisis mendalam pada dataset penyewaan sepeda (Bike Sharing Dataset) guna menemukan pola penggunaan sepeda berdasarkan berbagai kondisi serta memahami profil pelanggan.

## Profil Pengembang
- **Nama:** Shinta Khumaira
- **Email:** Banoffe1993@gmail.com
- **ID Dicoding:** maira_14

## Struktur Folder Proyek
- **/dashboard**: Berisi file `dashboard.py` untuk visualisasi data interaktif menggunakan Streamlit.
- **/data**: Berisi dataset mentah yang digunakan dalam analisis.
- `notebook.ipynb`: File Jupyter Notebook yang berisi proses lengkap mulai dari *Data Wrangling*, *EDA*, hingga *Explanatory Analysis*.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek.

## Alur Analisis (Notebook)
1.  **Data Wrangling**: 
    - *Gathering Data*: Memuat data dari sumber CSV.
    - *Assessing Data*: Memeriksa tipe data, *missing values*, dan duplikasi.
    - *Cleaning Data*: Melakukan pembersihan data agar siap dianalisis.
2.  **Exploratory Data Analysis (EDA)**: Mengeksplorasi hubungan antar variabel untuk mendapatkan wawasan awal.
3.  **Visualization & Explanatory Analysis**: Menjawab pertanyaan bisnis menggunakan teknik visualisasi data.
4.  **Conclusion**: Kesimpulan akhir dan rekomendasi berdasarkan hasil temuan.


## Cara Menjalankan Proyek

### 1. Menyiapkan Environment (Opsional tapi Disarankan)
Gunakan virtual environment agar tidak mengganggu sistem global Anda.
```bash
python -m venv venv
# Aktifkan venv (Windows)
.\venv\Scripts\activate
# Aktifkan venv (Mac/Linux)
source venv/bin/activate

### 2. Instalasi Library
pip install -r requirements.txt

### 3. Menjalankan Notebook
Buka editor  (seperti VS Code atau Jupyter Lab) dan jalankan file:
notebook.ipynb.

### 4. Menjalankan Dashboard Streamlit
streamlit run dashboard/dashboard.py

### Cara Menggunakan File Ini:
1.  Buka VS Code.
2.  Buat file baru di folder utama kamu (sejajar dengan `notebook.ipynb`) dan beri nama **`README.md`**.
3.  Salin seluruh teks di dalam kotak kode di atas dan tempelkan ke dalam file tersebut.
4.  Simpan (Save).

Jika kamu melihat file ini di GitHub atau VS Code (dengan *preview mode*), tampilannya akan menjadi sangat rapi dengan judul besar, daftar poin, dan blok kode yang mudah dibaca.

Struktur Repositori
.
├── dashboard/
│   └── dashboard.py      # Script utama untuk aplikasi Streamlit
│
├── data/
│   ├── day.csv           # Dataset dengan agregasi harian
│   └── hour.csv          # Dataset dengan agregasi per jam
│
├── notebook.ipynb        # Notebook Jupyter berisi proses analisis data secara lengkap
├── requirements.txt      # File daftar dependensi Python yang diperlukan
└── README.md             # Dokumentasi proyek (file ini)