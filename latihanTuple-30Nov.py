# Tuple adalah salah satu tipe data di tipe data di python yg digunakan untuk menyimpan sekumpulan data dalam satu variabel
# Mirip seperti list, akan tetapi bersifat immutable atau tidak dapat diubah-ubah
# Data tuple menggunakan tanda kurung () sedangkan data list menggunakan tanda kurawal []


# Menuliskan data tuple
# dataSiswa = ("Bintang", "Computer Engineer", 2025)

# #Akses Data

# print ("Nama :", dataSiswa[0]) # mengakses data tuple index ke 0 (Bintang
# print ("Jurusan :", dataSiswa[1]) # mengakses data tuple index ke 1 (Computer Engineer
# print ("Tahun Lulus :", dataSiswa[2]) # mengakses data tuple index ke 2 (2025)


# #unpacking 
# nama, jurusan, angkatan = dataSiswa
# print("\n Unpacking", nama, jurusan, angkatan)

# #Looping 
# print("\n Looping isi Tuple:")
# for item in dataSiswa:
#     print(item)

dataSiswa = [
    ('Bintang', 90, 80),
    ('Brian', 90, 70),
    ('Shinta', 80, 70),
    ('Shandy', 80, 80),
    ('Nanda', 90,90),
]

print("NilaiSiswa:")
for nama, uts, uas in dataSiswa:
    print(f"Nama: {nama}, UTS: {uts}, UAS: {uas}")

print("Nilai Akhir Siswa")
for nama, uts, uas in dataSiswa:
    nilaiAkhir = uts * 0.4 + uas * 0.6
    print(f"Nama: {nama}, Nilai Akhir: {nilaiAkhir }")

print("Grafek Nilai Siswa")
for nama, uts, uas in dataSiswa:
    print(f"Nama: {nama}, {uts * 0.4 + uas * 0.6}  ")

    if {nilaiAkhir > 85}:
        grade = "A"
    elif { 85 > nilaiAkhir >= 75}:
        grade = "B"
    elif { 75 > nilaiAkhir >= 60}:
        grade = "C"
    else:
        grade = "D"

    print(f"Nama: {nama}, Nilai Akhir: {nilaiAkhir }, Grade: {grade}")
    