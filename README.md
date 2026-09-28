# Sentiment Analyzer + Insight Generator

Mini Project Sesi 15 (Python Programming for AI - Batch 8) - Project 5 dari 5 opsi. Memprediksi sentimen review (positif/negatif/netral) memakai TF-IDF + Logistic Regression (Sesi 10), dengan Gemini API (Sesi 13) merangkum pola dari kumpulan review.

Cocok untuk peserta dengan latar belakang: bisnis digital, e-commerce, marketing.

**Catatan penting**: Gemini dipanggil untuk **rangkuman batch** (setelah beberapa review terkumpul) - BUKAN per review satu-satu. Ini menunjukkan perbedaan jelas: model klasik untuk prediksi per item (cepat, murah), LLM untuk narasi/insight (butuh konteks lebih luas, dipanggil lebih jarang untuk hemat API call).

## Status

Aplikasi ini **sudah 100% jadi** - kode prediksi dan pemanggilan Gemini API sudah lengkap. Yang perlu kamu isi hanya API key kamu sendiri (lihat "Menyiapkan API Key" di bawah). Cocok dipakai sebagai referensi belajar: baca `app.py` untuk lihat bagaimana klasifikasi teks (Sesi 10) dan Gemini API (Sesi 13) digabung, termasuk pola panggil LLM untuk rangkuman batch, bukan per-item.

## Struktur Folder

```
sentiment-analyzer/
├── app.py                  # Streamlit - dashboard (lengkap)
├── sentiment_model.pkl      # Pipeline TF-IDF + Logistic Regression terlatih
├── reviews_dataset.csv      # Dataset sintetis 300 review (3 kelas seimbang)
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalasi

Gunakan virtual environment agar paket project ini tidak bentrok dengan paket Python lain yang sudah terpasang di sistem kamu (mis. error `command not found: streamlit` atau `ImportError` pada scipy/sklearn biasanya disebabkan oleh instalasi global yang tercampur):

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Menyiapkan API Key

Buka `app.py`, ganti baris:

```python
api_key = "GANTI_DENGAN_API_KEY_ANDA"
```

dengan API key Gemini kamu sendiri. Lihat `Panduan_Gemini_API_Key_dan_Test.docx` di folder `Sesi13_AI_Generatif_dan_LLM_API/` kalau belum punya API key.

## Menjalankan

```bash
source .venv/bin/activate      # jika belum aktif
streamlit run app.py
```

## Troubleshooting

- **`zsh: command not found: streamlit`** — venv belum diaktifkan, atau instalasi sebelumnya masuk ke `~/Library/Python/...` yang tidak ada di PATH. Aktifkan venv (`source .venv/bin/activate`) lalu jalankan lagi, atau jalankan sementara dengan `python3 -m streamlit run app.py`.
- **`ImportError: dlopen(...) scipy/sparse/linalg/_propack/...` (macOS)** — ini bukan soal instalasi paket, tapi versi Python sistem yang sudah lama (mis. Python 3.10 rilis 2022) tidak kompatibel di level loader dengan versi macOS yang jauh lebih baru. Reinstall scipy/numpy **tidak** memperbaiki ini. Solusinya: pakai Python yang lebih baru, misalnya lewat Homebrew:
  ```bash
  brew install python@3.12
  rm -rf .venv
  /opt/homebrew/bin/python3.12 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  streamlit run app.py
  ```
- Untuk memastikan arsitektur venv sesuai mesin kamu, jalankan `python3 -c "import platform; print(platform.machine())"` dan `uname -m` — keduanya harus sama (mis. sama-sama `arm64` di Apple Silicon).

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 10 (klasifikasi teks), Sesi 13 (Gemini API), dan Sesi 14 (Streamlit deployment).
