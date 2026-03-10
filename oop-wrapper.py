class Book:
    def __init__(self, title, quantity, author, price):
        self.judul = title
        self.kuantitas = quantity
        self.penulis = author
        self.harga = price

    def __repr__(self):
        return f'Book: {self.judul}, Quantity: {self.kuantitas}, Authors: {self.penulis}, Price: {self.harga}'
    

buku1 = Book('Hello Beautiful', 54, 'Ann Napolitano', 279736)
buku2 = Book('Generations', 98, 'Jean M. Twenge, Ph.D.', 372981)
buku3 = Book('King A Life', 76, 'Jonathan Eig', 419472)



print('')
print('============================================================')
print('                         Buku Pertama                       ')
print('============================================================')
print(buku1)
print('')

print('')
print('============================================================')
print('                         Buku Kedua                       ')
print('============================================================')
print(buku2)
print('')

print('')
print('============================================================')
print('                         Buku Ketiga                        ')
print('============================================================')
print(buku3)
print('')




