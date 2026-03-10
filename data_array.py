# Array adalah sekumpulan data di dalam sebuah variabel atau sebuah variabel,
# atau sebuah variabel memiliki  banyak data nilai.

# memanggil library array
import array as arr

# deklarasi variable angka untuk menampung data array
# bentuk umum array = .array(typecode, elements)
# typecode kali ini adalah 'i' yaitu signed int
# angka = arr.array('i', [1,2,3,4,5,6,7,8,9,])

# typecode ini adalah  'd' yaitu data (float)
angka = arr.array('d', [17.4, 25.6, 38.9])


# print(angka)
# print(len(angka))
# print(type(angka))

# mencetak dengan index data array
# print(angka[0])  # Output: 17.4
# print(angka[1])  # Output: 25.6
# print(angka[2])  # Output: 38.9
# print(angka[-1]) # Output: 38.9
# print(angka[-2]) # Output: 25.6
# print(angka[-3]) # Output: 17.4

# untuk mencari index baris dari nilai data array
# print(angka.index(25.6))

print('')
print('=============================')
print('Mencetak Array dengan perulangan for pada looping')
print('=============================')
#mencetak array dengan for

for data in angka: 
    print(data)

# membuat pembatas data kosong diakhir baris
print('')
