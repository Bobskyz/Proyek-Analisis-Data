# E-Commerce Public Dataset - Proyek Analisis Data

Proyek analisis data e-commerce Brazil yang mencakup eksplorasi data, visualisasi, dan dashboard interaktif.

**Nama:** Dafin Surya  
**Email:** dafinsurya111@gmail.com  
**ID Dicoding:** CDCC282D6Y2676

---

## 📊 Tentang Proyek

Proyek ini menganalisis dataset e-commerce public Brazil yang mencakup data dari Oktober 2016 hingga Agustus 2018. Analisis berfokus pada:

1. **Tren Pendapatan Bulanan** - Mengidentifikasi pola dan tren pendapatan bulanan dari transaksi yang berhasil (delivered)
2. **Kualitas Produk & Ulasan** - Mengevaluasi hubungan antara skor ulasan dengan volume pesanan per kategori produk
3. **Segmentasi Pelanggan (RFM)** - Menganalisis Recency, Frequency, dan Monetary untuk customer segmentation

---

## 📁 Struktur Folder

```
Proyek-Analisis-Data/
├── notebook.ipynb                      # Notebook analisis lengkap
├── requirements.txt                    # Daftar library Python yang diperlukan
├── README.md                           # File dokumentasi ini
├── url.txt                             # URL deployment dashboard
├── dashboard/                          # Folder aplikasi dashboard Streamlit
│   ├── dashboard.py                    # Script dashboard interaktif
│   ├── orders_dataset.csv              # Data order (raw)
│   ├── order_items_dataset.csv         # Data item per order (raw)
│   ├── order_payments_dataset.csv      # Data pembayaran (raw)
│   ├── order_reviews_dataset.csv       # Data review produk (raw)
│   ├── products_dataset.csv            # Data produk (raw)
│   └── product_category_name_translation.csv  # Terjemahan kategori
└── data/                               # Folder hasil export analisis
    ├── monthly_revenue.csv             # Pendapatan bulanan
    ├── orders_revenue.csv              # Pendapatan per pesanan
    ├── order_payments_grouped.csv      # Pembayaran yang dikelompokkan
    ├── category_stats.csv              # Statistik kategori produk
    ├── top_categories.csv              # Top 10 kategori dengan skor tertinggi
    ├── bottom_categories.csv           # 10 kategori dengan skor terendah
    ├── orders_products_reviews.csv     # Data pesanan dengan kategori & review
    └── rfm_analysis.csv                # Analisis RFM pelanggan
```

---

## 🔧 Instalasi

### Prasyarat
- **Python 3.13.13** (atau versi kompatibel)
- **VS Code** dengan extension Jupyter dan Python Debugger
- **pip** (Python package manager)

### Langkah-langkah Instalasi

1. **Pastikan Python 3.13.13 Terinstall**:
   ```powershell
   python --version
   ```
   Output seharusnya: `Python 3.13.13`

2. **Buka Terminal/PowerShell** dan navigasi ke folder proyek (Sesuaikan dengan path direktori masing-masing):
   ```powershell
   cd "c:\Users\ASUS\Documents\Coding Camp Powered by DBS Foundation (Data Scientist)\Belajar Fundamental Analisis Data\Proyek Akhir"
   ```

3. **Buat Virtual Environment (Opsional tapi Direkomendasikan)**:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Dependencies dari requirements.txt**:
   ```powershell
   pip install -r requirements.txt
   ```VS Code (Direkomendasikan) ⭐

**Environment Setup:**
- **Kernel Python**: 3.13.13
- **Editor**: Visual Studio Code
- **Extensions**: Jupyter, Python, Python Debugger

**Langkah-langkah:**

1. **Buka file notebook** di VS Code:
   ```powershell
   code notebook.ipynb
   ```

2. **Pilih Python Kernel**:
   - Klik tombol kernel selector di bagian atas notebook (biasanya tertulis "Python 3.x.x")
   - Pilih **Python 3.13.13** dari daftar yang tersedia
   - Atau gunakan command palette: `Ctrl + Shift + P` → "Python: Select Kernel" → Pilih 3.13.13

3. **Jalankan Cells**:
   - Klik tombol ▶️ (Run Cell) untuk menjalankan cell individual
   - Tekan `Shift + Enter` untuk menjalankan cell dan lanjut ke cell berikutnya
   - Tekan `Ctrl + Alt + Enter` untuk menjalankan cell tanpa pindah

4. **Jalankan Semua Cells** (Run All):
   - Klik ⏩ (Run All Cells) di toolbar notebook
   - Atau gunakan command palette: `Ctrl + Shift + P` → "Notebook: Run All Cells"

### Alternative: Menggunakan Jupyter Notebook

Jika ingin menggunakan Jupyter Notebook di browser:

```powershell
jupyter notebook
```

Kemudian buka `notebook.ipynb` dari browser.

1. **Buka file** `notebook.ipynb` dari browser yang terbuka

2. **Jalankan setiap cell** secara berurutan atau gunakan `Run All`:
   - Menu: `Cell` → `Run All`
   - Atau tekan `Ctrl + A` lalu `Shift + Enter`

### Menggunakan VS Code

1. Buka file `notebook.ipynb` di VS Code
2. Pilih Python kernel di bagian atas notebook
3. Jalankan cells dengan mengklik tombol ▶️ atau tekan `Shift + Enter`

---

## 🎨 Menjalankan Dashboard

Dashboard interaktif dibangun dengan **Streamlit** dan memungkinkan visualisasi data secara real-time dengan filter interaktif.

### Menjalankan Dashboard

1. **Pastikan Anda sudah install dependencies** (lihat bagian [Instalasi](#instalasi))

2. **Buka Terminal/PowerShell** dan navigasi ke folder proyek (Sesuaikan dengan path direktori masing-masing):
   ```powershell
   cd "c:\Users\ASUS\Documents\Coding Camp Powered by DBS Foundation (Data Scientist)\Belajar Fundamental Analisis Data\Proyek Akhir"
   ```

3. **Pastikan virtual environment aktif** (jika dibuat):
   ```powershell
   venv\Scripts\activate
   ```

4. **Jalankan Dashboard dari folder dashboard**:
   ```powershell
   streamlit run dashboard/dashboard.py
   ```

5. **Browser akan membuka otomatis** dengan URL `http://localhost:8501`

### Fitur Dashboard

- **📈 Tren Pendapatan Bulanan**: Visualisasi line chart pendapatan dengan filter tahun
- **⭐ Skor Ulasan per Kategori**: Bar chart interaktif dengan opsi tampilkan Top 10 & Bottom 10 atau semua kategori
- **📊 Metrik Utama**: Total pendapatan, rata-rata pendapatan bulanan, dan total pesanan
- **📋 Tabel Data Detail**: Tabel interaktif dengan sortir dan format currency

### Menghentikan Dashboard

Tekan `Ctrl + C` di terminal untuk menghentikan server Streamlit.

---

## 📊 Export Data & Folder Data

Notebook menghasilkan file analisis yang sudah diekspor ke format CSV untuk kemudahan penggunaan lebih lanjut:

### File Export (Folder `data/`)

| File | Deskripsi |
|------|-----------|
| `monthly_revenue.csv` | Pendapatan bulanan dengan breakdown per bulan (Oktober 2016 - Agustus 2018) |
| `orders_revenue.csv` | Detail pendapatan setiap pesanan yang berhasil delivered |
| `order_payments_grouped.csv` | Pembayaran yang dikelompokkan dan diagregasi |
| `category_stats.csv` | Statistik kategori produk: rata-rata review score dan jumlah order |
| `top_categories.csv` | Top 10 kategori dengan skor review tertinggi |
| `bottom_categories.csv` | 10 kategori dengan skor review terendah |
| `orders_products_reviews.csv` | Data lengkap pesanan dengan kategori produk dan review score |
| `rfm_analysis.csv` | Hasil analisis RFM (Recency, Frequency, Monetary) pelanggan |

Semua file dapat digunakan untuk analisis lanjutan atau integration dengan tool BI lainnya.

---

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
