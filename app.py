import os
import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Konfigurasi Sektor Internasional (Mock Data Generator Meta)
SECTORS = {
    "United States": {"count": 54148, "center": [37.0902, -95.7129], "spread": 15},
    "United Kingdom": {"count": 22172, "center": [55.3781, -3.4360], "spread": 4},
    "Germany": {"count": 1888, "center": [51.1657, 10.4515], "spread": 3},
    "China": {"count": 6431, "center": [35.8617, 104.1954], "spread": 12},
    "Japan": {"count": 3901, "center": [36.2048, 138.2529], "spread": 3},
    "Indonesia": {"count": 1317, "center": [-0.7893, 113.9213], "spread": 5}
}

# Ingestion Framework Cache (Menyimpan 95k+ node di dalam memori)
CACHED_NODES = []

def initialize_global_ingestion():
    """
    Simulasi Modular Ingestion Framework.
    Menghasilkan ~95k titik data kamera secara efisien untuk keperluan rendering performa tinggi.
    """
    global CACHED_NODES
    if CACHED_NODES:
        return

    print("[*] ARGUS Pipeline: Ingesting global data feeds...")
    node_id = 1
    
    # Kumpulan contoh URL stream video publik/terbuka untuk simulasi interaktif
    sample_streams = [
        {"type": "Live Video", "url": "https://sample.vodobox.net/skate_phantom_flex_4k/skate_phantom_flex_4k.m3u8"},
        {"type": "Live Video", "url": "https://diceyk6a7mf78.cloudfront.net/hls/bhm.m3u8"},
        {"type": "Static Feed", "url": "https://picsum.photos/id/15/800/450"}
    ]

    for country, info in SECTORS.items():
        center_lat, center_lon = info["center"]
        
        # Optimasi memori: loop pembuatan titik koordinat massal
        for _ in range(info["count"]):
            # Sebarkan koordinat di sekitar pusat negara
            lat = center_lat + random.uniform(-info["spread"], info["spread"])
            lon = center_lon + random.uniform(-info["spread"], info["spread"])
            
            # Tentukan jenis stream secara acak berbobot (seperti pada gambar: mayoritas static)
            feed_choice = random.choices(sample_streams, weights=[15, 10, 75], k=1)[0]
            
            node = {
                "id": f"ARG-{node_id:06d}",
                "name": f"NODE.{random.randint(10,99)} @ {country.upper()}",
                "lat": round(lat, 4),
                "lon": round(lon, 4),
                "sector": country,
                "type": feed_choice["type"],
                "url": feed_choice["url"],
                "status": "Active" if random.random() > 0.02 else "Offline"
            }
            CACHED_NODES.append(node)
            node_id += 1
            
    print(f"[+] ARGUS Pipeline: Successfully loaded {len(CACHED_NODES)} surveillance nodes.")

@app.route('/')
def dashboard():
    """Halaman utama dashboard taktis"""
    return render_template('index.html')

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Mengembalikan metrik sistem global"""
    total = len(CACHED_NODES)
    live_count = sum(1 for n in CACHED_NODES if n["type"] == "Live Video")
    static_count = total - live_count
    
    sector_data = []
    for k, v in SECTORS.items():
        sector_data.append({"name": k, "count": v["count"]})

    return jsonify({
        "total_nodes": f"{total:,}",
        "system_status": "Active",
        "live_video": f"{live_count:,}",
        "static_feed": f"{static_count:,}",
        "sectors": sector_data
    })

@app.route('/api/nodes', methods=['GET'])
def get_nodes_geojson():
    """
    Mengonversi data koordinat internal ke format GeoJSON standard.
    Diberikan batasan limit data / pemotongan spasial agar browser tidak mengalami crash.
    """
    sector_filter = request.args.get('sector', None)
    
    features = []
    # Jika filter kosong, kita ambil sampel acak agar transfer data awal ke peta ringan
    nodes_to_render = CACHED_NODES
    if sector_filter and sector_filter in SECTORS:
        nodes_to_render = [n for n in CACHED_NODES if n["sector"] == sector_filter]
    else:
        # Batasi maksimal 8.000 titik acak di pandangan pertama global agar tidak lag di memori browser
        nodes_to_render = random.sample(CACHED_NODES, min(len(CACHED_NODES), 8000))

    for node in nodes_to_render:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [node["lon"], node["lat"]]
            },
            "properties": {
                "id": node["id"],
                "name": node["name"],
                "type": node["type"],
                "url": node["url"],
                "sector": node["sector"]
            }
        })

    return jsonify({
        "type": "FeatureCollection",
        "features": features
    })

if __name__ == '__main__':
    initialize_global_ingestion()
    app.run(host='0.0.0.0', port=5000, debug=True)
