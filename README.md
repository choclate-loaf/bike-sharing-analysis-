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

## Pertanyaan Bisnis yang Dijawab
- Pada kondisi seperti apa total peminjaman sepeda mencapai titik tertinggi dalam kurun waktu 2 tahun?
- Bagaimana perbandingan jumlah penyewa sepeda yang terdaftar sebagai pelanggan tetap (*registered*) dibandingkan dengan pelanggan biasa (*casual*)?

## Library yang Digunakan
Proyek ini menggunakan library Python berikut:
- `pandas`: Untuk manipulasi dan analisis data.
- `matplotlib` & `seaborn`: Untuk pembuatan visualisasi data (grafik).
- `streamlit`: Untuk membangun dashboard interaktif.

## Cara Menjalankan Proyek

### 1. Menyiapkan Environment (Opsional tapi Disarankan)
Gunakan virtual environment agar tidak mengganggu sistem global Anda.
```bash
python -m venv venv
# Aktifkan venv (Windows)
.\venv\Scripts\activate
# Aktifkan venv (Mac/Linux)
source venv/bin/activate


Tentu, ini adalah draf berkas README.md yang disusun secara profesional dan komprehensif berdasarkan isi file notebook.ipynb milikmu (Proyek Analisis Data Bike Sharing).

Berkas ini sudah mencakup panduan instalasi, struktur proyek, dan ringkasan analisis yang telah kamu lakukan.

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

## Pertanyaan Bisnis yang Dijawab
- Pada kondisi seperti apa total peminjaman sepeda mencapai titik tertinggi dalam kurun waktu 2 tahun?
- Bagaimana perbandingan jumlah penyewa sepeda yang terdaftar sebagai pelanggan tetap (*registered*) dibandingkan dengan pelanggan biasa (*casual*)?

## Library yang Digunakan
Proyek ini menggunakan library Python berikut:
- `pandas`: Untuk manipulasi dan analisis data.
- `matplotlib` & `seaborn`: Untuk pembuatan visualisasi data (grafik).
- `streamlit`: Untuk membangun dashboard interaktif.

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


