## 🛰️ ARGUS - Tactical Surveillance Dashboard

### *High-Performance Geospatial Analytics & Global Open-Data Camera Stream Aggregator*
Brought to you by **SPY-E** & **123Tool** ---

`ARGUS` adalah aplikasi dasbor pengawasan taktis berkinerja tinggi yang dirancang untuk mengumpulkan, memproses, dan memvisualisasikan data spasial dari umpan kamera data terbuka (*open-source camera feeds*) secara global. Alat ini memfasilitasi pemantauan waktu nyata (*real-time monitoring*) berskala besar terhadap **95.838++ node kamera** yang tersebar di jalan raya, landmark, dan pusat kota di seluruh dunia.

Dengan menggabungkan pustaka peta berbasis akselerasi perangkat keras (**MapLibre GL Vector Engine**) di sisi frontend dan **Modular Ingestion Framework** berbasis Python di sisi backend, platform ini menjamin rendering puluhan ribu data secara bersamaan tanpa lag (*Zero Bottleneck / Smooth 60 FPS Target*).

---

## 🔥 Fitur Utama

* **Global Surveillance Scale:** Visualisasi komprehensif untuk ~95,838 node aktif yang terbagi ke dalam 120+ sektor internasional (AS, Inggris, Jerman, China, Jepang, Indonesia).
* **GPU-Accelerated Geospatial Rendering:** Pemetaan taktis interaktif memanfaatkan akselerasi GPU via MapLibre GL dengan sistem *Dynamic Clustering Engine* otomatis untuk mencegah beban memori browser berlebih.
* **Adaptive Stream Processing:** Manajemen penanganan umpan multimedia cerdas yang mendukung pemutaran video streaming langsung (*Low-Latency HLS/M3U8*) menggunakan `Hls.js` serta pemrosesan gambar statis berfrekuensi tinggi (*High-Frequency Static Imaging*).
* **Modular Ingestion Framework:** Pipeline berbasis Python Flask yang efisien untuk menyimulasikan agregasi data massal, standarisasi koordinat, serta penyajian data dalam format standardisasi spasial GeoJSON.
* **Dark Cyberpunk Tactical Glassmorphic UI:** Antarmuka modern yang futuristik, bersih, berkelas, dan dioptimalkan secara responsif agar ramah ketika diakses melalui perangkat desktop maupun seluler.

---

## 🛠️ Panduan Instalasi & Konfigurasi

Ikuti langkah-langkah di bawah ini untuk memasang dan menjalankan dasbor ARGUS di lingkungan server lokal atau VPS Anda:

### 1. Kloning Repositori
Langkah pertama, unduh kode sumber proyek dari repositori GitHub:
```bash
git clone [https://github.com/username-lu/argus-dashboard.git](https://github.com/username-lu/argus-dashboard.git)
cd argus-dashboard
