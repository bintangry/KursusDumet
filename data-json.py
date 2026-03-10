# mengimport module request dan json yg sudah diinstall dengan pip install requests
import requests
import json

# URL API yang akan diambil datanya di limit sebanyak 2 saja
url = "https://dummyjpython -m pip install requestsson.com/products?limit=2"

# Melakukan permintaan HTTP GET ke API
response = requests.get(url)

# mEMERIKSA APAKAH PERMINTAAN BERHASIL (KODE STATUS 200)
if response.status_code == 200:
    # mengkonversikan response ke format JSON
    data_json = response.json()

    # menampilkan data JSON (jika argumen kedua adalah indent maka format tampilannya berantakan)
    print(json.dumps(data_json, indent=4))

else:
    # menampilkan pesan kesalahan jika permintaan tidak berhasil
    print("Gagal mendapatkan data. Kode Status:", response.status_code)