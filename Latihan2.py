harga = 50000         # int
jumlah = 3            # int
diskon = 0.10         # float

# using aritmatic
# diskon 10%

print(f"Harga total diskon seluruhnya: {harga * (1 - diskon) * jumlah}")
print(f"Harga total diskon seluruhnya: {harga - (harga * diskon) * jumlah}")

gaji_pokok = 3000000
tunjangan = 500000
bonus = 200000
potongan = 150000

# hitunglah gaji pokok karyawan setelah tunjangan, bonus, dan potongan
gajiBersih = gaji_pokok + tunjangan + bonus - potongan 

print(f" Gaji bersih karyawan adalah: {gajiBersih}")
