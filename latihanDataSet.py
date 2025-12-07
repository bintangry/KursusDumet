# Dataset adalah sekumpulan data yang biasanya disimpan dalam bentuk:

# 1. daftar (list)
# 2. tuple
# 3. dictionary


# Di python DataSet bukan tipe data khusus, akan tetapi sekumpulan data yang terstruktur yang digunakan untuk analisa dan pemrosesan data

# DataSet Berbentuk List of tuple

# dataSiswa = {
#     ('Bintang', 85, 90),
#     ('Brian', 90, 95),
#     ('Shinta', 90, 75),

# }

# print("DataSet Siswa:")
# for nama, uts, uas in dataSiswa:
#     print(f"Nama: {nama}, UTS: {uts}, UAS: {uas}")

# Dataset Berbentuk List of Dictionary

# dataSiswa = {
#     'id': [1,2,3,4,5],
#     'nama':['Bintang', 'Brian', 'Shinta', 'Rakha', 'Shandy'],
#     'kota':['Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi'],

# }

# print("Nama Siswa: ", dataSiswa['nama'])

# Dataset Menggunakan Pandas DataFrame
# Pandas adalah library python untuk mengolah data dalam bentuk table

# import pandas as pd

# # Membuat dataset berbentuk table (Dataframe)
# dataSiswa = {
#     'id': [1,2,3,4,5],
#     'nama':['Bintang', 'Brian', 'Shinta', 'Rakha', 'Shandy'],
#     'kota':['Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi'],

# }

# dataSet = pd.DataFrame(dataSiswa)
# print(dataSet)

dataKoordinat = (
    (-6.200000, 106.816666),
    (-7.250445, 112.768845),
    (-6.914744, 107.609810),
)

print("Koordinat Kota Besar di Indonesia:")
print(dataKoordinat)
print("-" * 40)

latitude = dataKoordinat[0][0]
longitude = dataKoordinat[0][1]

# Mengambil dan Menampilkan Posisi pertama
print(f"Latitude:{latitude}, Longitude: {longitude}")
print("-" * 40)

#unpacking tuple untuk posisi kedua
