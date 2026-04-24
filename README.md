# E-Commerce Public Dataset - Proyek Analisis Data

Proyek analisis data e-commerce Brazil yang mencakup eksplorasi data, visualisasi, dan dashboard interaktif.

**Nama:** Dafin Surya  
**Email:** dafinsurya111@gmail.com  
**ID Dicoding:** CDCC282D6Y2676

---

## 📋 Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Struktur Folder](#struktur-folder)
- [Instalasi](#instalasi)
- [Menjalankan Analisis Notebook](#menjalankan-analisis-notebook)
- [Menjalankan Dashboard](#menjalankan-dashboard)
- [Pertanyaan Bisnis & Insight](#pertanyaan-bisnis--insight)

---

## 📊 Tentang Proyek

Proyek ini menganalisis dataset e-commerce public Brazil yang mencakup data dari Oktober 2016 hingga Agustus 2018. Analisis berfokus pada:

1. **Tren Pendapatan Bulanan** - Mengidentifikasi pola dan tren pendapatan bulanan dari transaksi yang berhasil (delivered)
2. **Kualitas Produk & Ulasan** - Mengevaluasi hubungan antara skor ulasan dengan volume pesanan per kategori produk
3. **Segmentasi Pelanggan (RFM)** - Menganalisis Recency, Frequency, dan Monetary untuk customer segmentation

---

## 📁 Struktur Folder

```
Proyek Akhir/
├── Proyek_Analisis_Data.ipynb          # Notebook analisis lengkap
├── dashboard.py                         # Dashboard interaktif Streamlit
├── requirements.txt                     # Daftar library Python yang diperlukan
├── README.md                           # File dokumentasi ini
└── E-Commerce Public Dataset/          # Folder dataset
    ├── customers_dataset.csv
    ├── geolocation_dataset.csv
    ├── order_items_dataset.csv
    ├── order_payments_dataset.csv
    ├── order_reviews_dataset.csv
    ├── orders_dataset.csv
    ├── product_category_name_translation.csv
    ├── products_dataset.csv
    └── sellers_dataset.csv
```

---

## 🔧 Instalasi

### Prasyarat
- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah-langkah Instalasi

1. **Buka Terminal/Command Prompt** dan navigasi ke folder proyek:
   ```bash
   cd "c:\Users\ASUS\Documents\Coding Camp Powered by DBS Foundation (Data Scientist)\Belajar Fundamental Analisis Data\Proyek Akhir"
   ```

2. **Buat Virtual Environment (Opsional tapi direkomendasikan)**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📓 Menjalankan Analisis Notebook

### Menggunakan Jupyter Notebook

1. **Buka Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Buka file** `Proyek_Analisis_Data.ipynb` dari browser yang terbuka

3. **Jalankan setiap cell** secara berurutan atau gunakan `Run All`:
   - Menu: `Cell` → `Run All`
   - Atau tekan `Ctrl + A` lalu `Shift + Enter`

### Menggunakan VS Code

1. Buka file `Proyek_Analisis_Data.ipynb` di VS Code
2. Pilih Python kernel di bagian atas notebook
3. Jalankan cells dengan mengklik tombol ▶️ atau tekan `Shift + Enter`

---

## 🎨 Menjalankan Dashboard

Dashboard interaktif dibangun dengan **Streamlit** dan memungkinkan visualisasi data secara real-time dengan filter interaktif.

### Menjalankan Dashboard

1. **Pastikan Anda sudah install dependencies** (lihat bagian [Instalasi](#instalasi))

2. **Buka Terminal/Command Prompt** dan navigasi ke folder proyek:
   ```bash
   cd "c:\Users\ASUS\Documents\Coding Camp Powered by DBS Foundation (Data Scientist)\Belajar Fundamental Analisis Data\Proyek Akhir"
   ```

3. **Jalankan Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

4. **Browser akan membuka otomatis** (jika tidak, buka `http://localhost:8501`)

### Fitur Dashboard

- **📈 Tren Pendapatan Bulanan**: Visualisasi line chart pendapatan dengan filter tahun
- **⭐ Skor Ulasan per Kategori**: Bar chart interaktif dengan opsi tampilkan Top 10 & Bottom 10 atau semua kategori
- **📊 Metrik Utama**: Total pendapatan, rata-rata pendapatan bulanan, dan total pesanan
- **📋 Tabel Data Detail**: Tabel interaktif dengan sortir dan format currency

### Menghentikan Dashboard

Tekan `Ctrl + C` di terminal untuk menghentikan server Streamlit.

---

## 🎯 Pertanyaan Bisnis & Insight

### Pertanyaan 1: Tren Pendapatan Bulanan (2016-2018)

**Insight Utama:**
- Pendapatan menunjukkan tren pertumbuhan keseluruhan sepanjang periode
- **November 2017** mencatat pendapatan tertinggi (~1.1 juta)
- **Desember 2016** mencatat pendapatan terendah (data parsial, awal periode)
- Terlihat lonjakan signifikan di bulan-bulan tertentu (mungkin terkait kampanye seasonal)

### Pertanyaan 2: Rata-rata Skor Ulasan per Kategori

**Insight Utama:**
- Kategori **health_beauty** dan **sports_leisure** memiliki skor tertinggi (>4.2)
- Kategori **bed_bath_table**, **computers_accessories**, dan **furniture_decor** memiliki skor terendah (<4.0)
- Inverse relationship: Kategori dengan skor tinggi tidak selalu memiliki volume pesanan terbanyak
- Kategori dengan skor rendah cenderung memiliki volume pesanan yang lebih besar

### Analisis Tambahan: Segmentasi Pelanggan (RFM)

**Insight Kritis:**
- **One-Time Buyers Dominance**: Mayoritas pelanggan (Frequency = 1.0) hanya melakukan satu kali pembelian
- **Customer Inactivity**: Recency rata-rata 450-460 hari menunjukkan pelanggan sudah ~15 bulan tidak berbelanja
- **Tidak Ada Champions Sejati**: Tidak ada pelanggan dengan kombinasi Recency baru, Frequency tinggi, dan Monetary besar

**Rekomendasi Action Items:**
1. ⚠️ **Prioritas 1 - Meningkatkan Repeat Purchase**: Implementasikan strategi mendorong pembelian kedua dalam waktu singkat
2. 🔄 **Prioritas 2 - Re-activation Campaign**: Lakukan kampanye win-back untuk inactive customers (450+ hari)
3. 💡 **Prioritas 3 - Improve Customer Experience**: Analisis alasan low repeat rate untuk meningkatkan satisfaction

---

## 📞 Dukungan & Pertanyaan

Untuk pertanyaan atau bantuan, silakan hubungi:
- **Email**: dafinsurya111@gmail.com

---

## 📄 License

Dataset: E-Commerce Public Dataset (Brazilian E-Commerce) by Olist<br>
Proyek Akhir Kelas Belajar Fundamental Analisis Data Coding Camp

---

**Terakhir diperbarui**: April 2026
