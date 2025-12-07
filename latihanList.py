#Data list di python adalah struktur data yang berurutan yang dapat menyimpan banyak nilai didalamnya (dalam variabel), Data list bersifat Mutable atau dapat diubah-ubah
# dapat dimaninpulasi , dan untuk mengekses data list menggunakan index (dimulai dari 0)

buah = ['apel', 'mangga', 'jeruk', 'semangka']

print(f' Buah kesukaan saya adalah {buah[1]}') # mengakses data list index ke 1 (mangga)

# 1. menambah data list menggunakan method append() untuk menambah data diakhir list
buah.append('kiwi')
print(f' Buah kesukaan saya adalah {buah}')

# 2. menambahkan nilai baru di posisi tertentu menggunakan method insert(index, 'nilai baru')
buah.insert(2, 'nanas') # menambahkan nanas di index ke 2
print(f' Buah kesukaan saya adalah {buah}')

# 3. menggabungkan nilai data list dengan data list
sayurNew= ["wortel", "timun"]

# 4. menghapus nilai dengan mendefinisikan nilainya langsung tanpa indeks baris
buah.remove('apel')

# 5. mengambil nilai terakhir dari data list menggunakan method pop()
buah.pop() # menghapus data terakhir (kiwi)
del buah[0] # menghapus data index ke 0 (mangga)

# 6. bisa mengubah nilai menggunakan index baris -> mengubah data lama menjadi daata baru
sayurNew[0] = "bayam"

buah.extend(sayurNew) # menggabungkan data list sayurNew ke data list buah

# Note
#tidak bisa di replace jika ada extend di kode sebelumnya.

# Mencetaknya
print(f'Total Data list {len(buah)}')

# Mencetak otomatis semua data list menggunakan looping
for item in buah:
    print(f' Buah dan sayur kesukaan saya adalah {item}')


# STUDI KASUS Program Daftar Belanja 
daftarBelanja = []
while True:
    item = input(" Masukkan barang atau selesai")

    if item == 'selesai':
        break
    daftarBelanja.append(item)

print(f"\n Daftar Belanja Anda")
for barang in daftarBelanja:
    print('-', barang)
