# Membuat Class dengan nama book
class Book:
    # inisiasi saat class nanti di panggil ada dua buah parameter yang akan di isi
    def __init__(self, name, price):
        # Mendeklarasikan 2 buah properti
        self.judul = name
        self.harga = price
        
class Magazine(Book):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.judul_majalah = name
        self.harga_majalah = price

obj1 = Magazine('Start with Why', 150000)

print(obj1.judul)
