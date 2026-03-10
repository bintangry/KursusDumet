# Array adalah tipe data kompleks yang didalamnya disimpan banyak nilai lebih dari 1

# dataSiswa = ['Bintang', 'Brian','Rakha']

# print(f"Nama siswa a/n: {dataSiswa[0]}")

nama_siswa = [] #untuk membuat variabel data array kosong

jumlah = int(input("masukkan jumlah siswa: "))
for i in range(jumlah): # untuk membuat input 
    nama = input("Masukkan Nama siswa ke- " + str(i+1) + ": ") # membuat input user guna memasukkan siswa satur per satu
    nama_siswa.append(nama) #append adalah fungsi untuk menambahkan nilai ke dalam variabel nama_siswa

#tampilkan semua data
print("\n============ Daftar Siswa ========")
for index, nama in enumerate(nama_siswa):
    print(index+1, ",", nama)

# hitung total
print("\nTotal Siswa", len(nama_siswa)) # ldn adalah fungsi untuk menghitung jumlah baris didalam variable nama_siswa

      
cari = input("\nCari nama siswa: ")

if cari in nama_siswa:
   print("Nama ditemukan di index", nama_siswa.index(cari))

else:
   print("Nama tidak ditemukan")

hapus = input("\n Masukan nama yang ingin dihapus: ")
      
if hapus in nama_siswa:
   nama_siswa.remove(hapus)
   print("Nama berhasil dihapus")

else:
   print("Nama tidak ada")

#TAMPILAN DATA TERBARU
print("\n========= DATA TERBARU =======")
for i, nama in enumerate(nama_siswa):
   print(i+1, ".", nama)

   


