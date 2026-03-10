# Data produk
produk = [
    {"nama": "Keyboard", "harga": 150000},
    {"nama": "Mouse", "harga": 50000},
    {"nama": "Monitor", "harga": 1200000},
    {"nama": "Flashdisk", "harga": 40000},
    {"nama": "Headset", "harga": 250000}
]

# 1. Ambil produk dengan harga > 50.000
filter_produk = [p for p in produk if p["harga"] > 50000]

# 2. Hitung diskon 10% dan simpan harga barunya dan urutkan dari harga tertinggi
for p in filter_produk:
    p["harga_diskon"] = p["harga"] * 0.9

produk_urut = sorted(filter_produk, key=lambda x: x ["harga_diskon"], reverse = True)


# 3. Ambil hanya nama produk
hasil_akhir = [p["nama"] for p in produk_urut]

print(hasil_akhir)