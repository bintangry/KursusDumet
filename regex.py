# Regular expression (REGEX) adalah urutan karakter yang membentuk pola pencarian. 
# Modul yang umum digunakan untuk bekerja dengan regex di Python adalah re. 
# Berikut adalah beberapa dasar penggunaan regex di Python:

import re

company = 'PT. Duta Media Teknologi'
kata = re.compile(r'duta', re.IGNORECASE)
cek = kata.search(company)

print('')
print('nama perusahan: ', company)
print('Cek Kata: duta')

if cek:
    print('Benar ada dan sesuai')

else:
    print('Salah dan tidak sesuai')

# print('')
# print('Cek #2: duta')

# if cek2:
#     print('Benar ada dan sesuai')

# else:
#     print('Salah dan tidak sesuai')

# print('')

#Caps sensitive: angka kapital bisa mempengaruhi hasil kode


