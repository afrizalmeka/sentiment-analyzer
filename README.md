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

Gunakan virtual environment agar paket project ini tidak bentrok dengan paket Python lain yang sudah terpasang di sistem kamu (mis. error `command not found: streamlit` atau `ImportError` pada scipy/sklearn biasanya disebabkan oleh instalasi global yang tercampur atau versi Python yang sudah usang — lihat Troubleshooting):

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Windows (Command Prompt atau PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\activate
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
source .venv/bin/activate      # Windows: .venv\Scripts\activate — jika belum aktif
streamlit run app.py
```

Untuk keluar dari virtual environment kapan saja, jalankan `deactivate` (sama di macOS/Linux maupun Windows).

## Troubleshooting

- **`command not found: streamlit`** (macOS/Linux) atau **`streamlit tidak dikenali sebagai perintah internal...`** (Windows) — venv belum diaktifkan. Aktifkan dulu (`source .venv/bin/activate` di macOS/Linux, atau `.venv\Scripts\activate` di Windows) lalu jalankan lagi, atau jalankan sementara dengan `python -m streamlit run app.py` (Windows) / `python3 -m streamlit run app.py` (macOS/Linux).
- **`ImportError: dlopen(...) scipy/sparse/linalg/_propack/...`** — khusus **macOS**. Ini bukan soal instalasi paket, tapi versi Python sistem yang sudah lama (mis. Python 3.10 rilis 2022) tidak kompatibel di level loader dengan versi macOS yang jauh lebih baru. Reinstall scipy/numpy **tidak** memperbaiki ini. Solusinya: pakai Python yang lebih baru lewat Homebrew:
  ```bash
  brew install python@3.12
  rm -rf .venv
  /opt/homebrew/bin/python3.12 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  streamlit run app.py
  ```
  Untuk memastikan arsitektur venv sesuai mesin kamu, jalankan `python3 -c "import platform; print(platform.machine())"` dan `uname -m` — keduanya harus sama (mis. sama-sama `arm64` di Apple Silicon).
- **Windows: `running scripts is disabled on this system`** saat menjalankan `activate` di PowerShell — kebijakan eksekusi PowerShell memblokir script. Jalankan sekali saja (sebagai user biasa, tidak perlu admin):
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```
  lalu coba aktifkan venv lagi. Alternatif tanpa mengubah kebijakan: gunakan Command Prompt (`cmd.exe`) dan jalankan `.venv\Scripts\activate.bat`.
- **Windows: pastikan Python 3.10–3.12 terinstal dan tercentang "Add python.exe to PATH"** saat instalasi dari [python.org](https://www.python.org/downloads/windows/). Kalau `python` tidak dikenali di terminal, install ulang dengan opsi PATH tersebut dicentang, atau pakai `py -3.12 -m venv .venv` (Python Launcher) sebagai pengganti `python -m venv .venv`.

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 10 (klasifikasi teks), Sesi 13 (Gemini API), dan Sesi 14 (Streamlit deployment).
