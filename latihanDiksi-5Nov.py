# 5 November 2025
# Dictionary adalah salah satu tipe data di python yang digunakan untuk menyimpan data dalam bentuk pasangan kunci dan nilai (key-value pairs).
# Ciri khas dari dictionary:
# 1. Ditulis menggunakan kurung kurawal {}
# 2. Menggunakan pasangan key:Value
# 3. key harus unik (tidak boleh ada yang sama)
# 4. value boleh dengan tipe data apapun (string, integer, list, tuple, bahkan dictionary lagi)

# Diksi adalah pilihan kata yang tepat dan efektif dalam menyampaikan pesan atau makna tertentu.
# Dalam menulis atau berbicara, penggunaan diksi yang baik dapat meningkatkan kualitas
# komunikasi dan membuat pesan lebih jelas serta menarik bagi audiens.

# DataSiswa = {
# 'nama_lengkap' : 'Bintang Arya', 
# 'usia' : 21,
# 'jenis_kelamin' : 'Laki-laki',
# 'email': 'aryapradipta.bintang99@gmail.com',
# 'telepon': '082233445566',
# 'alamat': 'Jl. Merpati No. 123, Jakarta',
# 'status kesiswaan': True
#  }

# # print(DataSiswa['nama_lengkap'])

# #hanya cetak nilainya saja
# # for key in DataSiswa:
# #     print(DataSiswa[key])

# #mencetak key dan nilainya
# for key, value in DataSiswa.items():
#     print(key, ":" ,value)

# gaji = {
#     "brian": 5000000,
#     "toni": 4500000,
#     "indra": 6000000,
#     "sinta": 5500000
# }
# #menghitung total gaji karyawan
# # total_gaji = 0
# # for key, value in gaji.items():
# #     total_gaji += value
# #     print(key, ":", value)
# # print("Total Gaji Karyawan: Rp", format(total_gaji, ","))

# #cari gaji tertinggi
# gaji_tertinggi = 0
# karyawan_tertinggi = 0
# for key, value in gaji.items():
#     if value > gaji_tertinggi:
#         gaji_tertinggi = value
#         karyawan_tertinggi = key   
# print(karyawan_tertinggi, format(gaji_tertinggi, ","))

gaji = {
    "brian": 5000000,
    "toni": 4500000,
    "indra": 6000000,
    "sinta": 5500000,
    "Bintang": 13000000,
}

total = 0
gaji_tertinggi = 0
nama_tertinggi = ""

# Loop semua data
for nama, nilai in gaji.items():
    total += nilai                   # Hitung total gaji

    if nilai > gaji_tertinggi:       # Cari gaji tertinggi
        gaji_tertinggi = nilai
        nama_tertinggi = nama

print("Total Gaji :", total)
print("Gaji Tertinggi :", gaji_tertinggi)
print("Nama Karyawan :", nama_tertinggi)