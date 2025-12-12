# Dictionary adalah sebuah cara untuk menyimpan sebuah kunci dan nilai 
# (key and value) dalam satu variabel.

# Beberapa cara
# 1. Tuples
# 2. List 
# 3. Set
# 4. Dictionary

# membuat dictionary dengan nama variabel student
student = {
    'id': 1,
    'fullname': 'Dumet School',

    #tidak diizinkan duplicate untuk key-nya
    'year':2013,
    #jika sama maka yang diambil adalah yang terakhir
    'year':2023,
    'languages': ['ID','EN','FR']

}

# mencetak tipe data
print(type(student))
# untuk mencetak total data
print(len(student))
# mencetak data student
print(student)
# mencetak nilai dari ket year
print(student['year'])
# mencetak nilai dari key id
print(student.get('id'))

# mendapat semua nilai dan mencetaknya
data = student.values()
print(data)

# mendapat semua key:value dan mencetaknya
all = student.items()
print(all)

# cek dan cetak jika key fullname ada maka akan meencetaknya
if 'fullname' in student:
    print("yes, 'fullname' is one of the keys in the student dictionary.")


# cara pertama mengubah nilai di dictionary
student['id'] = 2
print(student)

# cara kedua mengubah nilai di dictionary
student.update({'fullname':'Dumet School Jakarta'})
print(student)

# cara menambah data (key/value) di dictionary
student['email'] = 'dumetschool123@gmail.com'
print(student)

 #cara kedua menambah data (key/value) di dictionary
student.update({'whatsapp':'08123456789'})
print(student)

# untuk menghapus data di dictionary
student.pop('languages')
print(student)

student.popitem() #menghapus data terakhir yakni whatsapp
print(student)

# cara kedua menghapus data di dictionary secara spesifik
del student['year']
print(student)


# cara keempat menghapus semua data di dictionary
student.clear()
print(student)


