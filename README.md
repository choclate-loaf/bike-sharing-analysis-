# 🚲 Bike Sharing Dashboard ✨

## Setup Environment - Anaconda
conda create --name bike-ds python=3.9
conda activate bike-ds
pip install -r requirements.txt


## Setup Environment - Shell/Terminal
cd "C:\Users\marsi\Downloads\submission 3"

Membuat virtual environment

python -m venv venv

Aktivasi virtual environment (Windows)

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt


## Run streamlit app
streamlit run dashboard.py


---

## 📌 Catatan
- Pastikan folder `data` berisi `day.csv` dan `hour.csv`
- Jika terjadi error streamlit, jalankan:
python -m streamlit run dashboard.py