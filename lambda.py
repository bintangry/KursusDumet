# cara mmebuat fungsi di python dengan keyword def
def penjumlahan(x,y):
    #   kita kembalikan nilai totalknya
    return x + y

#   cetak output dengan memanggil fungsinya
print(penjumlahan(1,2))

# membuat variabel dengan nama pertambahan
# konversi baris diatas menjadi lambda function
pertambahan = lambda x,y: x + y

# cetak output dengan memanggil lambda function-nya
print(pertambahan(3,4))

# membuat variabel dengan nama perkalian
# membuat formula untuk perkalian
perkalian = lambda a: a * 5

# cetak output dengan memanggil lamda 
print(perkalian(8))

# kali ini kita akan mencoba dengan tipe data string
domain = 'dumetschool.com'

# method .upper() akan membuat tulisan menjadi kapital semuanya
data = lambda teks: teks.upper()

# cetak output dengan memanggil lambda function-nya
print(data(domain))

# Implementasi looping dengan menggunakan loop
angka = [lambda argumen = x: argumen * 10 for x in range (1, 6)]

# lambda argumen = 1: arfumen * 10
# lambda argumen = 2: argumen * 10
# lambda argumen = 3: argumen * 10
# lambda argumen = 4: argumen * 10
# lambda argumen = 5: argumen * 10
# sampai ke 6

# maka dapat di simpulkan nilai angkanya adalah
# angka = [ 10, 20, 30, 40, 50 ]


# kita looping 
for item in angka:
    # cetak output
    print(item())
