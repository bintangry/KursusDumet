# conditional adalah suatu metode yang sudah pasti tersedia di semua bahasa 
# pemrograman, dan sebagai dasar menjalankan program pada kondisi yang berbeda

# kondisi terkait logika
#  a == b
# a != b
# a > b
# a < b
# a >= b
# a <= b  

# deklarasikan variabel

x = 1
y = 2

# cek apakah nilai y lebih besar dari x

if y > x:
    print(f'Benat {y} lebih besar dari {x}.')

if y < x: 
    #cetak output jika kondisi diatas adalah benar
    #karena operator yang digunakan adalah <
    #dan hasil dari kondisinya adalah salah
    #maka output ini tidak akan tercetak
    print(f'Benar {y} lebih kecil dari {x}.')

elif y > x:
    #cetak output jika kondisi ini benar
    print(f'Ya benar, {y} lebih besar dari {x}.')

else:
    #maka output ini yang akan tercetak jika kondisi diatas adalah salah
    print(f'Salah, {y} tidak lebih kecil dari {x}.')





