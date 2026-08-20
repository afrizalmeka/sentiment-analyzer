"""
app.py - Sentiment Analyzer + Insight Generator (Sesi 15 - Mini Project).

Prediksi sentimen review (positif/negatif/netral) memakai TF-IDF +
Logistic Regression (Sesi 10), dengan Gemini API (Sesi 13) merangkum
pola dari kumpulan review - dipanggil untuk RANGKUMAN BATCH, bukan
per review satu-satu, supaya hemat API call.

Jalankan dengan:
    streamlit run app.py
"""
import sqlite3

import joblib
import pandas as pd
import streamlit as st
from google import genai

st.title("Sentiment Analyzer + Insight Generator")
st.write("Prediksi sentimen review (positif/negatif/netral) memakai TF-IDF + Logistic Regression (Sesi 10), dengan Gemini API merangkum pola dari beberapa review sekaligus.")

# Ganti dengan API key Gemini kamu sendiri (lihat Panduan_Gemini_API_Key_dan_Test.docx
# di folder Sesi13 kalau belum punya).
api_key = "GANTI_DENGAN_API_KEY_ANDA"

# Model berupa Pipeline lengkap (TF-IDF + Logistic Regression jadi satu),
# jadi cukup panggil .predict() langsung dengan teks mentah.
model = joblib.load("sentiment_model.pkl")

client = genai.Client(api_key=api_key)

DB_PATH = "riwayat_sentimen.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS review (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teks_review TEXT,
            sentimen TEXT
        )
        """
    )
    conn.commit()
    conn.close()


init_db()

st.write("### Input Review")
with st.form("form_review"):
    teks_review = st.text_area("Tulis review produk/layanan", placeholder="Contoh: Produk ini sangat bagus, saya puas!")
    submit = st.form_submit_button("Analisis Sentimen")

if submit and teks_review:
    sentimen = model.predict([teks_review])[0]

    st.write("### Sentimen:", sentimen)

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO review (teks_review, sentimen) VALUES (?, ?)",
        (teks_review, sentimen),
    )
    conn.commit()
    conn.close()

st.write("### Distribusi Sentimen (dari SQLite)")
conn = sqlite3.connect(DB_PATH)
riwayat_df = pd.read_sql_query("SELECT * FROM review ORDER BY id DESC", conn)
conn.close()

if not riwayat_df.empty:
    st.bar_chart(riwayat_df["sentimen"].value_counts())
    st.dataframe(riwayat_df)
else:
    st.info("Belum ada review yang dianalisis.")

# Gemini API dipanggil untuk merangkum POLA dari SEMUA review yang
# terkumpul (bukan per review satu-satu) - hanya saat tombol diklik,
# dan WAJIB dibungkus try/except.
if st.button("Buat Insight dari Semua Review") and not riwayat_df.empty:
    st.write("### Insight dari Gemini")
    try:
        semua_review = "\n".join(riwayat_df["teks_review"].tolist())
        prompt = (
            f"Berikut kumpulan review pelanggan:\n\n{semua_review}\n\n"
            f"Rangkum dalam 3-4 kalimat: pola umum apa yang muncul, "
            f"apa keluhan utama (jika ada), dan apa yang paling disukai (jika ada)."
        )
        response = client.models.generate_content(model="gemini-3.5-flash", contents=prompt)
        st.write(response.text)
    except Exception as e:
        st.warning(f"Insight LLM tidak tersedia saat ini ({e}). Distribusi sentimen di atas tetap valid.")
