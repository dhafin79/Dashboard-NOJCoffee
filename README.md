# ☕ Dashboard NOJ Coffee

### Analisis Performa Produk Menggunakan RFM dan K-Means Clustering

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)

Dashboard interaktif untuk menganalisis **performa dan segmentasi produk NOJ Coffee** berdasarkan data transaksi penjualan menggunakan metode **RFM (Recency, Frequency, Monetary)** dan **K-Means Clustering**.

---

## 📌 Tentang Proyek

Proyek ini dikembangkan sebagai bagian dari penelitian tugas akhir dengan judul:

> **"Analisis Segmentasi Produk Pada NOJ Coffee Menggunakan Metode RFM dan K-Means Clustering Berbasis Dashboard"**

Dashboard digunakan untuk membantu menyajikan hasil pengolahan data transaksi menjadi informasi yang lebih mudah dipahami melalui visualisasi dan segmentasi produk.

Analisis dilakukan dengan mengelompokkan produk berdasarkan karakteristik:

* **Recency** — seberapa baru suatu produk terakhir terjual.
* **Frequency** — seberapa sering suatu produk terjual.
* **Monetary** — total nilai penjualan yang dihasilkan suatu produk.

Hasil pengelompokan menggunakan K-Means digunakan untuk mengidentifikasi karakteristik performa produk.

---

## 🎯 Tujuan

Dashboard ini bertujuan untuk:

1. Mengolah data transaksi penjualan menjadi data analisis produk.
2. Menghitung nilai **Recency, Frequency, dan Monetary (RFM)**.
3. Mengelompokkan produk berdasarkan karakteristik RFM menggunakan **K-Means Clustering**.
4. Menyajikan hasil segmentasi melalui dashboard interaktif.
5. Membantu memberikan gambaran mengenai performa produk berdasarkan data transaksi.

---

## 📊 Metode RFM

RFM digunakan untuk menggambarkan karakteristik performa setiap produk berdasarkan data transaksi.

| Variabel      | Pengertian                          | Pengukuran                                                |
| ------------- | ----------------------------------- | --------------------------------------------------------- |
| **Recency**   | Waktu sejak produk terakhir terjual | Jarak antara tanggal transaksi terakhir dan tanggal acuan |
| **Frequency** | Frekuensi penjualan produk          | Jumlah transaksi produk                                   |
| **Monetary**  | Nilai penjualan produk              | Total nilai penjualan produk                              |

### Recency

Recency menunjukkan seberapa baru suatu produk terakhir kali terjual.

Semakin **kecil nilai Recency**, semakin baru produk tersebut mengalami transaksi penjualan.

### Frequency

Frequency menunjukkan seberapa sering suatu produk muncul dalam transaksi.

Semakin **tinggi Frequency**, semakin sering produk tersebut terjual.

### Monetary

Monetary menunjukkan total nilai penjualan yang dihasilkan oleh suatu produk.

Semakin **tinggi Monetary**, semakin besar kontribusi nilai penjualan produk tersebut.

---

## 🤖 K-Means Clustering

Setelah nilai RFM diperoleh, data distandardisasi sebelum digunakan dalam proses clustering.

Metode **K-Means Clustering** digunakan untuk mengelompokkan produk berdasarkan kemiripan karakteristik RFM.

Jumlah cluster ditentukan menggunakan **Elbow Method**.

Hasil analisis menghasilkan **3 cluster produk**.

### 🏆 Produk Laris

Produk dengan karakteristik:

* Recency relatif rendah.
* Frequency tinggi.
* Monetary tinggi.
* Menunjukkan performa penjualan paling baik.

### 📈 Produk Potensial

Produk dengan karakteristik RFM berada pada tingkat menengah.

Produk dalam kelompok ini memiliki potensi untuk dikembangkan berdasarkan pola penjualannya.

### 📉 Produk Kurang Laku

Produk dengan karakteristik:

* Recency relatif tinggi.
* Frequency lebih rendah.
* Monetary lebih rendah.
* Menunjukkan performa penjualan yang relatif rendah.

---

## 📈 Dashboard

Dashboard dikembangkan menggunakan **Streamlit** untuk menyajikan hasil analisis secara interaktif.

Dashboard mencakup beberapa informasi seperti:

* Ringkasan data transaksi.
* Hasil perhitungan RFM.
* Distribusi karakteristik RFM.
* Hasil clustering.
* Informasi masing-masing segmen produk.
* Visualisasi hasil segmentasi.
* Daftar produk berdasarkan cluster.

---

## 🛠️ Teknologi yang Digunakan

| Teknologi                | Penggunaan                           |
| ------------------------ | ------------------------------------ |
| **Python**               | Bahasa pemrograman utama             |
| **Pandas**               | Pengolahan dan manipulasi data       |
| **Scikit-learn**         | Standardisasi dan K-Means Clustering |
| **Streamlit**            | Pengembangan dashboard interaktif    |
| **Matplotlib / Seaborn** | Visualisasi data                     |
| **Git & GitHub**         | Version control dan repository       |

---

## 📁 Struktur Project

```text
Dashboard-NOJCoffee/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

> Dataset transaksi asli tidak disertakan dalam repository karena mengandung data internal penelitian.

---

## 🔐 Data Privacy

Dataset transaksi yang digunakan dalam penelitian **tidak disertakan dalam repository publik**.

Hal ini dilakukan untuk menjaga kerahasiaan data transaksi dan informasi internal NOJ Coffee.

File yang mengandung data pribadi atau data transaksi internal juga tidak seharusnya diunggah ke repository publik.

---

## 🎓 Research Context

Proyek ini merupakan implementasi dari penelitian:

**Analisis Performa Produk Pada NOJ Coffee Menggunakan RFM dan K-Means Clustering**

Metodologi penelitian menggunakan pendekatan **CRISP-DM** yang meliputi:

```text
Business Understanding
        ↓
Data Understanding
        ↓
Data Preparation
        ↓
Modeling
        ↓
Evaluation
        ↓
Deployment
```

Dashboard Streamlit digunakan sebagai tahap implementasi untuk menyajikan hasil analisis secara interaktif.

---

## 👨‍💻 Author

**Dhafin Fadhilah**

Information Systems Student
Universitas Gunadarma

GitHub: [@dhafin79](https://github.com/dhafin79)

---

## 📄 License

Project ini dibuat untuk keperluan **akademik dan penelitian**.

© 2026 Dhafin Fadhilah
