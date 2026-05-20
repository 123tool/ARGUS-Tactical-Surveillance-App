## ARGUS - Tactical Surveillance Dashboard

### *High-Performance Geospatial Analytics & Global Open-Data Camera Stream Aggregator*
Brought to you by **SPY-E** & **123Tool** ---

`ARGUS` adalah aplikasi dasbor pengawasan taktis berkinerja tinggi yang dirancang untuk mengumpulkan, memproses, dan memvisualisasikan data spasial dari umpan kamera data terbuka (*open-source camera feeds*) secara global. Alat ini memfasilitasi pemantauan waktu nyata (*real-time monitoring*) berskala besar terhadap **95.838++ node kamera** yang tersebar di jalan raya, landmark, dan pusat kota di seluruh dunia.

Dengan menggabungkan pustaka peta berbasis akselerasi perangkat keras (**MapLibre GL Vector Engine**) di sisi frontend dan **Modular Ingestion Framework** berbasis Python di sisi backend, platform ini menjamin rendering puluhan ribu data secara bersamaan tanpa lag (*Zero Bottleneck / Smooth 60 FPS Target*).

---

## Fitur :
* **Global Surveillance Scale:** Visualisasi komprehensif untuk ~95,838 node aktif yang terbagi ke dalam 120+ sektor internasional (AS, Inggris, Jerman, China, Jepang, Indonesia).
* **GPU-Accelerated Geospatial Rendering:** Pemetaan taktis interaktif memanfaatkan akselerasi GPU via MapLibre GL dengan sistem *Dynamic Clustering Engine* otomatis untuk mencegah beban memori browser berlebih.
* **Adaptive Stream Processing:** Manajemen penanganan umpan multimedia cerdas yang mendukung pemutaran video streaming langsung (*Low-Latency HLS/M3U8*) menggunakan `Hls.js` serta pemrosesan gambar statis berfrekuensi tinggi (*High-Frequency Static Imaging*).
* **Modular Ingestion Framework:** Pipeline berbasis Python Flask yang efisien untuk menyimulasikan agregasi data massal, standarisasi koordinat, serta penyajian data dalam format standardisasi spasial GeoJSON.

---

## 🛠️ Instalasi & Konfigurasi

Ikuti langkah-langkah di bawah ini untuk memasang dan menjalankan dasbor ARGUS di lingkungan server lokal atau VPS Anda:

## 1. Clone
Langkah pertama, unduh kode sumber proyek dari repositori GitHub :
```bash
git clone https://github.com/123tool/ARGUS-Tactical-Surveillance-App.git
cd ARGUS-Tactical-Surveillance-App
```
## 2. Instalasi Dependensi
​Pastikan sistem Anda sudah terpasang Python versi 3.9 ke atas, lalu instal micro-framework Flask sebagai dependensi utama server backend :
```
pip install flask
```
## Menjalankan
​Langkah 1 : Inisialisasi Pipeline & Start Server
​Jalankan server utama app.py lewat terminal atau console server Anda :
```
python3 app.py
```
Saat pertama kali dijalankan, Modular Ingestion Framework akan otomatis memproses data dan memuat seluruh node ke dalam sistem memori cache :
```
[*] ARGUS Pipeline: Ingesting global data feeds...
[+] ARGUS Pipeline: Successfully loaded 95,838 surveillance nodes.
* Running on http://all-interfaces:5000/ (Press CTRL+C to quit)
```
Langkah 2 : Akses Dashboard via Browser
Buka browser modern pilihan Anda (sangat disarankan menggunakan Google Chrome, Microsoft Edge, atau browser berbasis Chromium lainnya yang mendukung akselerasi perangkat keras/WebGL).

Akses alamat lokal server berikut :
```
http://127.0.0.1:5000
```
## Navigasi Taktis Peta
- ​Zooming & Clustering : Gunakan roda gulir mouse atau cubitan layar pada smartphone untuk memperbesar wilayah. Titik kamera akan secara dinamis menyatu menjadi kluster angka besar jika dijauhkan, dan akan memecah menjadi titik-titik kamera individu yang presisi saat didekatkan.
- ​Sector Filtering : Pada panel kanan bawah (Sector Filter), klik salah satu nama negara (seperti Indonesia atau United Kingdom) untuk mengunci fokus kamera satelit dan memperbarui visualisasi titik kamera khusus pada sektor tersebut secara instan.
- Live Monitoring : Klik pada salah satu titik kamera tunggal berwarna cyan/biru di peta. Panel monitor di sebelah kiri akan langsung terbuka secara otomatis untuk menghubungkan tautan, memutar video live streaming, atau memperbarui gambar telemetri wilayah tersebut secara real-time.
  
## Disclaimer

**Seluruh visualisasi node dan tautan video yang digunakan di dalam rilis dasar ini ditujukan sebagai bentuk simulasi teknis, pengujian performa beban rendering browser, serta demonstrasi**
