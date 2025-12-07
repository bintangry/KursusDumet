
# e-module
# 1. Aritmatika 

a = 10
b = 7

print(f"Hasil menjumlahkan: {a + b}") # menjumlahkan
print(f"Hasil mengurangi: {a - b}") # mengurangi
print(f"Hasil perkalian: {a * b}") # perkalian
print(f"Hasil pembagian: {a / b}") # pembagian
print(f"Hasil modulus: {a % b}") # modulus / sisa bagi
print(f"Hasil pangkat: {a ** b}") # pangkat
print(f"Hasil pembulatan kebawah: {a // b}") # pembulatan kebawah

# f yang ada didalam print adalah kunci khusus yang wajib disertakan jika ingin mencetak variabel didalam area tanda kutip dengan catatan dibungkus pakai {variabel}

# 2. Comparison Opeartor / Operator Perbandingan (Hanya menghasilkan 2 nilai True dan false jika salah)

x = 90
print (x ==80) #False
print (x !=80) #True #Tidak sama dengan
print (x >80)  #True
print (x <80)  #False
print (x >=80) #True
print (x <=80) #False 

# 3. Logical Operator (Operator yang menghubungkan beberapa perbandingan)
# untuk menggabungkan ekspresi boolean

# and (True jika 2 kondisi benar), or  (True jika salah satunya saja yang benar), not (mengbalik nilai boolean)

usia = 20
print(usia > 18 and usia == 20) #True (karena kedua kondisi logika sama sama benar)
print(usia > 18 or usia == 90) #True (karena salah satu kondisi logika benar)
print(not usia == 20) # False (karena nilai boolean dibalik)
