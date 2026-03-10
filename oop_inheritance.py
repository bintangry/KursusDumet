class Matematika:
    # Membuat property dengan nama x
    x = 1

# membuat inheritance class baru yang diwariskan dari class Matematika
class Penjumlahan(Matematika):
    # Mendeklarasikan nilai dari property x yg diubah menjadi menjadi 2
    x = 2

# Membuat instance terhadap class penjumlahan
obj= Penjumlahan()


# untuk mencetak instance menjadi object yang selanjutnya akan memanggil sebuah property yang ada didalam class
print(obj.x)
