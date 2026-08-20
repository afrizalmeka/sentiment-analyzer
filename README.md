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

```bash
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
streamlit run app.py
```

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 10 (klasifikasi teks), Sesi 13 (Gemini API), dan Sesi 14 (Streamlit deployment).
